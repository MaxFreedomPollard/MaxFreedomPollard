#!/usr/bin/env python3
"""Fetch live Kaggle competition rankings and render theme-adaptive SVG stripes."""

from __future__ import annotations

import argparse
import gzip
import http.cookiejar
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from collections.abc import Sequence
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from svg_stripes import render_kaggle_slices, render_kaggle_stripe  # noqa: E402

KAGGLE_BASE = "https://www.kaggle.com"
KAGGLE_RPC = f"{KAGGLE_BASE}/api/i"
KAGGLE_PROFILE_URL = f"{KAGGLE_BASE}/maxfpollard"
LIVE_DATA_RAW_BASE = (
    "https://raw.githubusercontent.com/MaxFreedomPollard/MaxFreedomPollard/live-data"
)

SLICE_PREFIX = "kaggle-v2"
PINNED_FIRST_KEY = "ieee"
README_START_MARKER = "<!-- KAGGLE-LIVE-STRIPE:START -->"
README_END_MARKER = "<!-- KAGGLE-LIVE-STRIPE:END -->"

COMPETITIONS: tuple[dict, ...] = (
    {
        "key": "ieee",
        "label": "IEEE Big Data",
        "slug": "2026-ieee-big-data-traffic-flow-bench",
        "fallback_id": 153956,
        "seed": {"public_rank": 1, "private_rank": 23, "public_score": "0.93124", "total_teams": 802},
    },
    {
        "key": "neurips",
        "label": "NeurIPS Smart Buildings",
        "slug": "neurips-2026-smart-buildings",
        "fallback_id": 157303,
        "seed": {"public_rank": 31, "private_rank": None, "public_score": "0.00906", "total_teams": 522},
    },
    {
        "key": "quantum",
        "label": "Google Quantum AI",
        "slug": "google-verifiable-quantum-circuit-compilation",
        "fallback_id": 161954,
        "seed": {"public_rank": 42, "private_rank": None, "public_score": "33.29467", "total_teams": 3827},
    },
    {
        "key": "rogii",
        "label": "ROGII Wellbore",
        "slug": "rogii-2-wellbore-curve-tracing",
        "fallback_id": 181555,
        "seed": {"public_rank": 58, "private_rank": None, "public_score": "0.6825", "total_teams": 153},
    },
)

CANDIDATE_TEAM_NAMES = {
    "max pollard",
    "max freedom pollard",
    "maxfreedompollard",
    "maxfreedom",
}
CANDIDATE_HANDLES = {
    "maxfpollard",
    "maxfreedompollard",
    "maxpollard",
    "maxfreedom",
}


class KagglePublicClient:
    """Zero-secret client for Kaggle's public JSON web endpoints (`/api/i`)."""

    def __init__(self) -> None:
        self.jar = http.cookiejar.CookieJar()
        self.opener = urllib.request.build_opener(
            urllib.request.HTTPCookieProcessor(self.jar)
        )
        self.token = os.environ.get("KAGGLE_API_TOKEN", "").strip()
        self.xsrf = ""
        self._seed_session()

    def _base_headers(self) -> dict[str, str]:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
            ),
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip",
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    def _read_body(self, resp) -> bytes:
        raw = resp.read()
        if resp.headers.get("Content-Encoding", "").lower() == "gzip":
            return gzip.decompress(raw)
        return raw

    def _seed_session(self) -> None:
        req = urllib.request.Request(f"{KAGGLE_BASE}/", headers=self._base_headers())
        with self.opener.open(req, timeout=25) as resp:
            self._read_body(resp)
        for cookie in self.jar:
            if cookie.name == "XSRF-TOKEN" and cookie.value:
                self.xsrf = cookie.value
                break
        if not self.xsrf:
            raise RuntimeError("Did not receive XSRF-TOKEN cookie from kaggle.com.")

    def post(self, service_method: str, payload: dict, retries: int = 3) -> dict:
        url = f"{KAGGLE_RPC}/{service_method}"
        body = json.dumps(payload).encode("utf-8")
        headers = {
            **self._base_headers(),
            "Content-Type": "application/json",
            "X-XSRF-TOKEN": self.xsrf,
        }
        last_err: Exception | None = None
        for attempt in range(retries):
            try:
                req = urllib.request.Request(url, data=body, headers=headers, method="POST")
                with self.opener.open(req, timeout=40) as resp:
                    return json.loads(self._read_body(resp).decode("utf-8"))
            except Exception as exc:
                last_err = exc
                if attempt + 1 < retries:
                    time.sleep(2.0 * (attempt + 1))
        raise RuntimeError(f"Kaggle RPC {service_method} failed: {last_err}") from last_err


def _index_board(rows: list[dict] | None) -> dict[int, int]:
    """Map teamId -> official 1-based rank."""
    ranks: dict[int, int] = {}
    for pos, row in enumerate(rows or [], start=1):
        tid = row.get("teamId")
        if tid is None:
            continue
        r = row.get("rank")
        ranks[int(tid)] = int(r) if r is not None and int(r) > 0 else pos
    return ranks


def _find_team(
    teams: list[dict],
    known_handles: set[str],
    known_team_names: set[str],
) -> tuple[dict | None, set[str]]:
    discovered_handles = set(known_handles)
    # Pass 1: exact handle match in teamMembers
    for team in teams:
        members = team.get("teamMembers") or team.get("members") or []
        for m in members:
            uname = (m.get("userName") or "").strip().lower()
            dname = (m.get("displayName") or "").strip().lower()
            if uname and uname in discovered_handles:
                for m2 in members:
                    u2 = (m2.get("userName") or "").strip().lower()
                    if u2:
                        discovered_handles.add(u2)
                return team, discovered_handles
            if dname and dname in known_team_names:
                for m2 in members:
                    u2 = (m2.get("userName") or "").strip().lower()
                    if u2:
                        discovered_handles.add(u2)
                return team, discovered_handles

    # Pass 2: teamName match
    for team in teams:
        tname = (team.get("teamName") or "").strip().lower()
        if tname in known_team_names:
            for m in (team.get("teamMembers") or team.get("members") or []):
                uname = (m.get("userName") or "").strip().lower()
                if uname:
                    discovered_handles.add(uname)
            return team, discovered_handles

    return None, discovered_handles


def _fetch_competition_standing(
    client: KagglePublicClient,
    slug: str,
    fallback_id: int,
    known_handles: set[str],
    known_team_names: set[str],
) -> tuple[dict, set[str]]:
    comp_id = fallback_id
    total_teams_meta: int | None = None
    try:
        meta = client.post(
            "competitions.CompetitionService/GetCompetition",
            {"competitionName": slug},
        )
        comp_obj = meta.get("competition") if isinstance(meta.get("competition"), dict) else meta
        if comp_obj and comp_obj.get("id"):
            comp_id = int(comp_obj["id"])
        for k in ("totalTeams", "teamCount"):
            if comp_obj and comp_obj.get(k):
                total_teams_meta = int(comp_obj[k])
                break
    except Exception:
        pass

    board = client.post(
        "competitions.LeaderboardService/GetLeaderboard",
        {"competitionId": comp_id, "leaderboardMode": "LEADERBOARD_MODE_DEFAULT"},
    )
    teams = board.get("teams") or []
    pub_rows = board.get("publicLeaderboard") or []
    pub_ranks = _index_board(pub_rows)
    priv_ranks = _index_board(board.get("privateLeaderboard"))
    pub_scores = {
        int(row["teamId"]): row.get("displayScore")
        for row in pub_rows
        if row.get("teamId") is not None
    }

    total_teams = max(
        len(pub_ranks),
        len(priv_ranks),
        len(teams),
        total_teams_meta or 0,
    )

    team, updated_handles = _find_team(teams, known_handles, known_team_names)
    tid = int(team["teamId"]) if team and team.get("teamId") is not None else None
    result = {
        "slug": slug,
        "competition_id": comp_id,
        "team_id": tid,
        "team_name": team.get("teamName") if team else None,
        "public_rank": pub_ranks.get(tid) if tid is not None else None,
        "public_score": pub_scores.get(tid) if tid is not None else None,
        "private_rank": priv_ranks.get(tid) if tid is not None else None,
        "total_teams": total_teams,
    }
    return result, updated_handles


def _try_profile_entered_count(client: KagglePublicClient, handles: set[str]) -> tuple[str | None, int | None]:
    for handle in sorted(handles):
        try:
            res = client.post(
                "routing.RoutingService/GetPageDataByUrl",
                {"relativeUrl": f"/{handle}"},
            )
            prof = res.get("userProfile") or {}
            uname = prof.get("userName")
            if uname:
                # Check if competition summary count is present on profile payload
                comp_summary = prof.get("competitionsSummary") or {}
                total = comp_summary.get("totalResults") or comp_summary.get("count")
                return str(uname), (int(total) if total else None)
        except Exception:
            continue
    return None, None


def _format_public_standing(info: dict) -> tuple[str, str]:
    pub = info.get("public_rank")
    total = info.get("total_teams") or 0
    if pub:
        return f"#{pub:,}", (f"/ {total:,}" if total else "")
    return "Active", (f"({total:,} teams)" if total else "")


def _competition_sort_key(
    spec: dict,
    summary: dict,
    default_index: int,
) -> tuple[int, int, int, int]:
    """Order IEEE first, then remaining competitions ascending by public rank."""
    info = summary.get(spec["key"]) or {}
    pub_rank = info.get("public_rank")
    total_teams = info.get("total_teams") or 0
    is_not_pinned = 0 if spec["key"] == PINNED_FIRST_KEY else 1
    rank_val = int(pub_rank) if pub_rank is not None and int(pub_rank) > 0 else 10**9
    return (is_not_pinned, rank_val, -int(total_teams), default_index)


def order_competitions(summary: dict) -> list[dict]:
    """Return competitions starting with IEEE, then sorted by best public rank."""
    return [
        spec
        for _, spec in sorted(
            enumerate(COMPETITIONS),
            key=lambda pair: _competition_sort_key(pair[1], summary, pair[0]),
        )
    ]


def render_kaggle_readme_line(ordered_specs: Sequence[dict]) -> str:
    """Build the seamless single-line HTML snippet for README.md in ranked order."""
    parts = [
        (
            f'<a href="{KAGGLE_PROFILE_URL}"><picture>'
            f'<source media="(prefers-color-scheme: dark)" srcset="{LIVE_DATA_RAW_BASE}/{SLICE_PREFIX}-left-dark.svg">'
            f'<source media="(prefers-color-scheme: light)" srcset="{LIVE_DATA_RAW_BASE}/{SLICE_PREFIX}-left-light.svg">'
            f'<img alt="Kaggle profile (public leaderboards, updated every 15 minutes)" '
            f'src="{LIVE_DATA_RAW_BASE}/{SLICE_PREFIX}-left-light.svg" width="16%">'
            f"</picture></a>"
        )
    ]
    for pos, spec in enumerate(ordered_specs, start=1):
        key = spec["key"]
        slug = spec["slug"]
        label = spec["label"]
        slice_base = f"{LIVE_DATA_RAW_BASE}/{SLICE_PREFIX}-{key}-p{pos}"
        parts.append(
            f'<a href="{KAGGLE_BASE}/competitions/{slug}/leaderboard?tab=public"><picture>'
            f'<source media="(prefers-color-scheme: dark)" srcset="{slice_base}-dark.svg">'
            f'<source media="(prefers-color-scheme: light)" srcset="{slice_base}-light.svg">'
            f'<img alt="{label} public leaderboard" src="{slice_base}-light.svg" width="21%">'
            f"</picture></a>"
        )
    return "".join(parts)


def sync_readme(readme_path: Path, ordered_specs: Sequence[dict]) -> bool:
    """Update the Kaggle stripe block inside README.md if the ranked order changed."""
    content = readme_path.read_text(encoding="utf-8")
    pattern = re.compile(
        rf"(^[ \t]*{re.escape(README_START_MARKER)}\n)(.*?)(\n[ \t]*{re.escape(README_END_MARKER)})",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(content)
    if not match:
        raise RuntimeError(
            f"Could not find {README_START_MARKER} ... {README_END_MARKER} markers in {readme_path}"
        )
    indent = re.match(r"^[ \t]*", match.group(1)).group(0)
    new_line = f"{indent}{render_kaggle_readme_line(ordered_specs)}"
    if match.group(2) == new_line:
        return False
    updated = content[: match.start(2)] + new_line + content[match.end(2) :]
    readme_path.write_text(updated, encoding="utf-8")
    return True


def _prune_unused_v2_slices(
    output_dir: Path,
    active_filenames: set[str],
    readme_text: str,
) -> None:
    """Remove stale `kaggle-v2-*.svg` slices no longer referenced by README.md."""
    for path in output_dir.glob(f"{SLICE_PREFIX}-*.svg"):
        if path.name in active_filenames:
            continue
        if path.name in readme_text:
            continue
        path.unlink(missing_ok=True)


def render_from_summary(
    summary: dict,
    output_dir: Path,
    *,
    readme_path: Path | None = None,
) -> tuple[list[dict], bool]:
    ordered_specs = order_competitions(summary)
    comp_display: list[tuple[str, str, str, str]] = []
    for spec in ordered_specs:
        key = spec["key"]
        rank_text, sub_text = _format_public_standing(summary[key])
        comp_display.append((key, spec["label"], rank_text, sub_text))

    summary_out = {
        **summary,
        "order": [spec["key"] for spec in ordered_specs],
    }
    entered = int(summary_out.get("entered_count") or len(COMPETITIONS))

    output_dir.mkdir(parents=True, exist_ok=True)
    active_slice_files: set[str] = set()
    for theme in ("dark", "light"):
        svg = render_kaggle_stripe(
            theme,
            entered_count=entered,
            competitions=comp_display,
        )
        (output_dir / f"kaggle-{theme}.svg").write_text(svg, encoding="utf-8")

        slices = render_kaggle_slices(
            theme,
            entered_count=entered,
            competitions=comp_display,
        )
        for slice_name, slice_svg in slices.items():
            filename = f"{SLICE_PREFIX}-{slice_name}-{theme}.svg"
            active_slice_files.add(filename)
            (output_dir / filename).write_text(slice_svg, encoding="utf-8")

    (output_dir / "kaggle.json").write_text(
        json.dumps(summary_out, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    readme_changed = False
    if readme_path is not None:
        readme_changed = sync_readme(readme_path, ordered_specs)
        if not readme_changed:
            _prune_unused_v2_slices(
                output_dir,
                active_slice_files,
                readme_path.read_text(encoding="utf-8"),
            )

    return ordered_specs, readme_changed


def _load_existing_summary(output_dir: Path) -> dict:
    existing = output_dir / "kaggle.json"
    if not existing.exists():
        return {}
    try:
        data = json.loads(existing.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "assets",
    )
    parser.add_argument(
        "--readme",
        type=Path,
        default=None,
        help="Optional README.md path to reorder Kaggle leaderboard links when rankings change.",
    )
    parser.add_argument(
        "--seed-only",
        action="store_true",
        help="Render initial seed SVGs from verified baseline before first GitHub Action run.",
    )
    args = parser.parse_args()

    if args.seed_only:
        summary: dict = {
            "entered_count": len(COMPETITIONS),
            "kaggle_user": "maxfpollard",
        }
        for spec in COMPETITIONS:
            summary[spec["key"]] = {
                "slug": spec["slug"],
                "competition_id": spec["fallback_id"],
                **spec["seed"],
            }
        ordered_specs, readme_changed = render_from_summary(
            summary, args.output_dir, readme_path=args.readme
        )
        order_str = " > ".join(spec["key"] for spec in ordered_specs)
        print(f"Rendered seed Kaggle stripe SVGs (order={order_str}, readme_changed={readme_changed}).")
        return

    handles = set(CANDIDATE_HANDLES)
    team_names = set(CANDIDATE_TEAM_NAMES)
    env_user = os.environ.get("KAGGLE_USER", "").strip().lower()
    if env_user:
        handles.add(env_user)
    env_teams = os.environ.get("KAGGLE_TEAM_NAMES", "").strip()
    if env_teams:
        for part in env_teams.split(","):
            if part.strip():
                team_names.add(part.strip().lower())

    existing_summary = _load_existing_summary(args.output_dir)
    standings: dict[str, dict] = {}
    try:
        client = KagglePublicClient()
        for spec in COMPETITIONS:
            info, handles = _fetch_competition_standing(
                client, spec["slug"], spec["fallback_id"], handles, team_names
            )
            prev = existing_summary.get(spec["key"])
            if (
                info.get("team_id") is None
                and info.get("public_rank") is None
                and (info.get("total_teams") or 0) == 0
                and isinstance(prev, dict)
                and prev.get("public_rank") is not None
            ):
                print(
                    f"Warning: Empty leaderboard response for {spec['key']}; preserving previous standing."
                )
                info = prev
            standings[spec["key"]] = info
        canonical_user, profile_entered = _try_profile_entered_count(client, handles)
    except Exception as exc:
        if existing_summary:
            print(f"Warning: Kaggle fetch failed ({exc}); preserving existing snapshot.")
            return
        raise

    entered_count = max(
        len(COMPETITIONS),
        profile_entered or 0,
        sum(1 for c in standings.values() if c.get("team_id") is not None),
    )

    summary = {
        "entered_count": entered_count,
        "kaggle_user": canonical_user,
        **standings,
    }
    ordered_specs, readme_changed = render_from_summary(
        summary, args.output_dir, readme_path=args.readme
    )
    parts = ", ".join(
        f"{spec['label']}={_format_public_standing(standings[spec['key']])}"
        for spec in ordered_specs
    )
    print(
        f"Updated Kaggle stripe (user={canonical_user}, entered={entered_count}, "
        f"readme_changed={readme_changed}): {parts}"
    )


if __name__ == "__main__":
    main()
