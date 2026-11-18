#!/usr/bin/env python3
"""Fetch live Kaggle competition rankings and render theme-adaptive SVG stripes."""

from __future__ import annotations

import argparse
import gzip
import http.cookiejar
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from svg_stripes import render_kaggle_stripe  # noqa: E402

KAGGLE_BASE = "https://www.kaggle.com"
KAGGLE_RPC = f"{KAGGLE_BASE}/api/i"

IEEE_SLUG = "2026-ieee-big-data-traffic-flow-bench"
IEEE_ID_DEFAULT = 153956

QUANTUM_SLUG = "google-verifiable-quantum-circuit-compilation"
QUANTUM_ID_DEFAULT = 161954

CANDIDATE_TEAM_NAMES = {
    "max pollard",
    "max freedom pollard",
    "maxfreedompollard",
    "maxfreedom",
}
CANDIDATE_HANDLES = {
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
    pub_ranks = _index_board(board.get("publicLeaderboard"))
    priv_ranks = _index_board(board.get("privateLeaderboard"))

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


def _format_ieee(info: dict) -> tuple[str, str]:
    pub = info.get("public_rank")
    priv = info.get("private_rank")
    total = info.get("total_teams") or 0
    sub = f"(/{total:,})" if total else ""
    if pub and priv:
        return f"#{pub:,} pub · #{priv:,} priv", sub
    if priv:
        return f"#{priv:,} private", sub
    if pub:
        return f"#{pub:,} public", sub
    return "Entered", sub


def _format_quantum(info: dict) -> tuple[str, str]:
    pub = info.get("public_rank")
    priv = info.get("private_rank")
    total = info.get("total_teams") or 0
    if pub and priv and pub != priv:
        return f"#{pub:,} pub · #{priv:,} priv", (f"(/{total:,})" if total else "")
    if priv:
        return f"#{priv:,}", (f"(/{total:,})" if total else "")
    if pub:
        return f"#{pub:,}", (f"(/{total:,})" if total else "")
    return "Active", (f"({total:,} teams)" if total else "")


def render_from_summary(summary: dict, output_dir: Path) -> None:
    ieee = summary["ieee"]
    quantum = summary["quantum"]
    ieee_text, ieee_sub = _format_ieee(ieee)
    quantum_text, quantum_sub = _format_quantum(quantum)
    entered = int(summary.get("entered_count") or 2)

    output_dir.mkdir(parents=True, exist_ok=True)
    for theme in ("dark", "light"):
        svg = render_kaggle_stripe(
            theme,
            entered_count=entered,
            ieee_text=ieee_text,
            ieee_sub=ieee_sub,
            quantum_text=quantum_text,
            quantum_sub=quantum_sub,
        )
        (output_dir / f"kaggle-{theme}.svg").write_text(svg, encoding="utf-8")

    (output_dir / "kaggle.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "assets",
    )
    parser.add_argument(
        "--seed-only",
        action="store_true",
        help="Render initial seed SVGs from verified baseline before first GitHub Action run.",
    )
    args = parser.parse_args()

    if args.seed_only:
        summary = {
            "entered_count": 2,
            "kaggle_user": None,
            "ieee": {
                "slug": IEEE_SLUG,
                "competition_id": IEEE_ID_DEFAULT,
                "public_rank": 1,
                "private_rank": 23,
                "total_teams": 801,
            },
            "quantum": {
                "slug": QUANTUM_SLUG,
                "competition_id": QUANTUM_ID_DEFAULT,
                "public_rank": None,
                "private_rank": None,
                "total_teams": 3268,
            },
        }
        render_from_summary(summary, args.output_dir)
        print("Rendered seed Kaggle stripe SVGs.")
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

    try:
        client = KagglePublicClient()
        ieee_info, handles = _fetch_competition_standing(
            client, IEEE_SLUG, IEEE_ID_DEFAULT, handles, team_names
        )
        quantum_info, handles = _fetch_competition_standing(
            client, QUANTUM_SLUG, QUANTUM_ID_DEFAULT, handles, team_names
        )
        canonical_user, profile_entered = _try_profile_entered_count(client, handles)
    except Exception as exc:
        existing = args.output_dir / "kaggle.json"
        if existing.exists():
            print(f"Warning: Kaggle fetch failed ({exc}); preserving existing snapshot.")
            return
        raise

    entered_count = max(
        2,
        profile_entered or 0,
        sum(1 for c in (ieee_info, quantum_info) if c.get("team_id") is not None),
    )

    summary = {
        "entered_count": entered_count,
        "kaggle_user": canonical_user,
        "ieee": ieee_info,
        "quantum": quantum_info,
    }
    render_from_summary(summary, args.output_dir)
    print(
        f"Updated Kaggle stripe (user={canonical_user}): "
        f"entered={entered_count}, IEEE={_format_ieee(ieee_info)}, "
        f"Quantum={_format_quantum(quantum_info)}"
    )


if __name__ == "__main__":
    main()
