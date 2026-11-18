#!/usr/bin/env python3
"""Fetch live star, fork, repo, and merged-change totals across contributed repos."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from svg_stripes import render_oss_stripe  # noqa: E402

GITHUB_USER = "MaxFreedomPollard"
GITHUB_API = "https://api.github.com"

# Exclude awesome-lists and MCP directory catalogs so every counted repo is an
# engineering / software codebase.
CATALOG_REPO_RE = re.compile(r"(^|/|-)(awesome)(-|$)|mcp-registry", re.IGNORECASE)


def _is_counted_external_repo(full_name: str) -> bool:
    if not full_name or "/" not in full_name:
        return False
    if full_name.lower().startswith(f"{GITHUB_USER.lower()}/"):
        return False
    if CATALOG_REPO_RE.search(full_name):
        return False
    return True


def _get_token() -> str:
    for key in ("GITHUB_TOKEN", "GH_TOKEN"):
        val = os.environ.get(key, "").strip()
        if val:
            return val
    try:
        return subprocess.check_output(["gh", "auth", "token"], text=True).strip()
    except Exception as exc:
        raise RuntimeError("No GITHUB_TOKEN/GH_TOKEN available for GitHub API.") from exc


def _gh_request(path_or_url: str, token: str, payload: dict | None = None) -> dict:
    url = path_or_url if path_or_url.startswith("http") else f"{GITHUB_API}{path_or_url}"
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(
        url,
        data=data,
        method="POST" if data is not None else "GET",
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "Content-Type": "application/json",
            "User-Agent": "MaxFreedomPollard-Profile-LiveSync/1.0",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _fetch_graphql_contributed(token: str) -> dict[str, dict]:
    query = """
    query($login: String!, $cursor: String) {
      user(login: $login) {
        repositoriesContributedTo(
          first: 100
          after: $cursor
          includeUserRepositories: false
          privacy: PUBLIC
          contributionTypes: [COMMIT]
        ) {
          pageInfo { hasNextPage endCursor }
          nodes {
            nameWithOwner
            stargazerCount
            forkCount
            isPrivate
          }
        }
      }
    }
    """
    repos: dict[str, dict] = {}
    cursor: str | None = None
    while True:
        res = _gh_request(
            "/graphql",
            token,
            {"query": query, "variables": {"login": GITHUB_USER, "cursor": cursor}},
        )
        conn = res["data"]["user"]["repositoriesContributedTo"]
        for node in conn["nodes"] or []:
            if not node or node.get("isPrivate"):
                continue
            name = node["nameWithOwner"]
            if _is_counted_external_repo(name):
                repos[name.lower()] = {
                    "name": name,
                    "stars": int(node["stargazerCount"]),
                    "forks": int(node["forkCount"]),
                }
        if not conn["pageInfo"]["hasNextPage"]:
            break
        cursor = conn["pageInfo"]["endCursor"]
    return repos


def _fetch_merged_prs(token: str) -> tuple[set[str], set[tuple[str, str]]]:
    """Return (repo_full_names, unique_pr_keys) across all merged external PRs."""
    q = urllib.parse.quote(f"is:pr is:merged author:{GITHUB_USER} -user:{GITHUB_USER}")
    repos: set[str] = set()
    prs: set[tuple[str, str]] = set()
    page = 1
    while True:
        data = _gh_request(f"/search/issues?q={q}&per_page=100&page={page}", token)
        items = data.get("items") or []
        if not items:
            break
        for item in items:
            repo_url = item.get("repository_url", "")
            parts = repo_url.rstrip("/").split("/")
            if len(parts) < 2:
                continue
            full_name = f"{parts[-2]}/{parts[-1]}"
            if _is_counted_external_repo(full_name):
                repos.add(full_name)
                prs.add((full_name.lower(), f"pr#{item.get('number')}"))
        if len(items) < 100 or page >= 10:
            break
        page += 1
    return repos, prs


def _parse_readme_contributions(readme_path: Path) -> tuple[set[str], set[tuple[str, str]]]:
    if not readme_path.exists():
        return set(), set()
    text = readme_path.read_text(encoding="utf-8")
    if "## Merged contributions" in text:
        text = text.split("## Merged contributions", 1)[1]
        for stop in ("\n## ",):
            if stop in text:
                text = text.split(stop, 1)[0]
    repos: set[str] = set()
    changes: set[tuple[str, str]] = set()
    pattern = re.compile(
        r"https://github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)/(pull|commit)/([A-Za-z0-9]+)"
    )
    for repo, kind, ref in pattern.findall(text):
        if _is_counted_external_repo(repo):
            repos.add(repo)
            key = f"pr#{ref}" if kind == "pull" else f"commit@{ref[:12]}"
            changes.add((repo.lower(), key))
    return repos, changes


def _fetch_missing_repos(missing_names: list[str], token: str) -> dict[str, dict]:
    found: dict[str, dict] = {}
    for i in range(0, len(missing_names), 25):
        batch = missing_names[i : i + 25]
        aliases = []
        for idx, full in enumerate(batch):
            owner, name = full.split("/", 1)
            aliases.append(
                f'r{idx}: repository(owner: {json.dumps(owner)}, name: {json.dumps(name)}) '
                "{ nameWithOwner stargazerCount forkCount isPrivate }"
            )
        query = "query { " + " ".join(aliases) + " }"
        res = _gh_request("/graphql", token, {"query": query})
        for node in (res.get("data") or {}).values():
            if not node or node.get("isPrivate"):
                continue
            name = node["nameWithOwner"]
            if _is_counted_external_repo(name):
                found[name.lower()] = {
                    "name": name,
                    "stars": int(node["stargazerCount"]),
                    "forks": int(node["forkCount"]),
                }
    return found


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--readme",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "README.md",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "assets",
    )
    args = parser.parse_args()

    token = _get_token()
    try:
        repos = _fetch_graphql_contributed(token)
    except Exception as exc:
        print(f"Note: GraphQL repositoriesContributedTo skipped ({exc}); using PR/README list.")
        repos = {}
    pr_repos, pr_changes = _fetch_merged_prs(token)
    readme_repos, readme_changes = _parse_readme_contributions(args.readme)

    desired: dict[str, str] = {}
    for full_name in pr_repos | readme_repos:
        desired.setdefault(full_name.lower(), full_name)
    missing = [name for key, name in desired.items() if key not in repos]
    if missing:
        repos.update(_fetch_missing_repos(missing, token))

    all_changes = pr_changes | readme_changes
    repo_count = len(repos)
    merged_count = len(all_changes)
    total_stars = sum(r["stars"] for r in repos.values())
    total_forks = sum(r["forks"] for r in repos.values())

    args.output_dir.mkdir(parents=True, exist_ok=True)
    for theme in ("dark", "light"):
        svg = render_oss_stripe(
            theme,
            repo_count=repo_count,
            merged_count=merged_count,
            total_stars=total_stars,
            total_forks=total_forks,
        )
        (args.output_dir / f"oss-{theme}.svg").write_text(svg, encoding="utf-8")

    summary = {
        "repo_count": repo_count,
        "merged_count": merged_count,
        "total_stars": total_stars,
        "total_forks": total_forks,
    }
    (args.output_dir / "oss.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        f"Updated OSS stripe: {repo_count} repos, {merged_count} merged changes, "
        f"{total_stars:,} stars, {total_forks:,} forks"
    )


if __name__ == "__main__":
    main()
