#!/usr/bin/env python3
"""Shared SVG renderer for theme-adaptive GitHub profile live telemetry stripes."""

from __future__ import annotations

from html import escape

FONT_STACK = (
    "-apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Inter', "
    "'Segoe UI', Helvetica, Arial, sans-serif"
)

THEMES = {
    "dark": {
        "bg0": "#0B1120",
        "bg1": "#0F172A",
        "bg2": "#090D16",
        "border0": "#334155",
        "border1": "#1E293B",
        "divider": "#1E293B",
        "btn_bg0": "#162338",
        "btn_bg1": "#101A2C",
        "btn_border0": "#38BDF8",
        "btn_border0_op": "0.45",
        "btn_border1": "#334155",
        "btn_border1_op": "0.85",
        "btn_icon": "#38BDF8",
        "text_primary": "#F8FAFC",
        "text_label": "#E2E8F0",
        "text_secondary": "#94A3B8",
        "text_muted": "#64748B",
        "sky": "#38BDF8",
        "indigo": "#818CF8",
        "emerald": "#34D399",
        "gold": "#FBBF24",
        "kaggle": "#20BEFF",
        "glow_opacity": "0.10",
    },
    "light": {
        "bg0": "#FFFFFF",
        "bg1": "#F8FAFC",
        "bg2": "#F1F5F9",
        "border0": "#CBD5E1",
        "border1": "#E2E8F0",
        "divider": "#CBD5E1",
        "btn_bg0": "#FFFFFF",
        "btn_bg1": "#F1F5F9",
        "btn_border0": "#0284C7",
        "btn_border0_op": "0.38",
        "btn_border1": "#94A3B8",
        "btn_border1_op": "0.55",
        "btn_icon": "#0284C7",
        "text_primary": "#0F172A",
        "text_label": "#1E293B",
        "text_secondary": "#475569",
        "text_muted": "#64748B",
        "sky": "#0284C7",
        "indigo": "#4F46E5",
        "emerald": "#059669",
        "gold": "#D97706",
        "kaggle": "#0284C7",
        "glow_opacity": "0.06",
    },
}

KAGGLE_SLICES: dict[str, tuple[int, int]] = {
    "left": (0, 243),      # 27% of 900
    "ieee": (243, 288),    # 32% of 900
    "quantum": (531, 279), # 31% of 900
    "live": (810, 90),     # 10% of 900
}


def _card_frame(
    theme_name: str,
    accent_color: str,
    dividers: list[int],
    *,
    view_x: int = 0,
    view_w: int = 900,
    include_button_defs: bool = False,
) -> tuple[str, str]:
    t = THEMES[theme_name]
    div_lines = "\n  ".join(
        f'<line x1="{x}" y1="13" x2="{x}" y2="37" stroke="{t["divider"]}" stroke-width="1"/>'
        for x in dividers
    )
    btn_defs = ""
    if include_button_defs:
        btn_defs = f'''
    <linearGradient id="btnBg" x1="0" y1="9.5" x2="0" y2="40.5" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="{t['btn_bg0']}"/>
      <stop offset="100%" stop-color="{t['btn_bg1']}"/>
    </linearGradient>
    <linearGradient id="btnBorder" x1="0" y1="9.5" x2="0" y2="40.5" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="{t['btn_border0']}" stop-opacity="{t['btn_border0_op']}"/>
      <stop offset="100%" stop-color="{t['btn_border1']}" stop-opacity="{t['btn_border1_op']}"/>
    </linearGradient>'''

    head = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{view_w}" height="50" viewBox="{view_x} 0 {view_w} 50" fill="none">
  <defs>
    <linearGradient id="bg" x1="0" y1="3" x2="900" y2="47" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="{t['bg0']}"/>
      <stop offset="55%" stop-color="{t['bg1']}"/>
      <stop offset="100%" stop-color="{t['bg2']}"/>
    </linearGradient>
    <radialGradient id="glow" cx="120" cy="25" r="240" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="{accent_color}" stop-opacity="{t['glow_opacity']}"/>
      <stop offset="100%" stop-color="{accent_color}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="border" x1="450" y1="3" x2="450" y2="47" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="{t['border0']}"/>
      <stop offset="100%" stop-color="{t['border1']}"/>
    </linearGradient>{btn_defs}
    <clipPath id="clip">
      <rect x="1" y="3" width="898" height="44" rx="10"/>
    </clipPath>
  </defs>

  <g clip-path="url(#clip)">
    <rect x="1" y="3" width="898" height="44" rx="10" fill="url(#bg)"/>
    <rect x="1" y="3" width="898" height="44" fill="url(#glow)"/>
  </g>
  <rect x="1" y="3" width="898" height="44" rx="10" stroke="url(#border)" stroke-width="1"/>
  {div_lines}'''
    return head, "</svg>\n"


def render_oss_stripe(
    theme_name: str,
    *,
    repo_count: int,
    merged_count: int,
    total_stars: int,
    total_forks: int,
) -> str:
    t = THEMES[theme_name]
    head, tail = _card_frame(theme_name, t["indigo"], [246, 438, 642, 808])

    repos_txt = f"{repo_count:,}"
    merged_txt = f"{merged_count:,}"
    stars_txt = f"{total_stars:,}"
    forks_txt = f"{total_forks:,}"

    body = f'''
  <!-- Left label: Git PR/merge badge + REPOS CONTRIBUTED TO -->
  <rect x="16" y="16" width="18" height="18" rx="4.5" fill="{t['indigo']}" fill-opacity="0.16"/>
  <g transform="translate(19, 19)" stroke="{t['indigo']}" stroke-width="1.45" stroke-linecap="round" stroke-linejoin="round" fill="none">
    <circle cx="3" cy="3" r="1.7"/>
    <circle cx="3" cy="9.5" r="1.7"/>
    <circle cx="9.2" cy="9.5" r="1.7"/>
    <path d="M3 4.7V7.8"/>
    <path d="M4.7 3C7.3 3 9.2 4.8 9.2 7.8"/>
  </g>
  <text x="41" y="29" fill="{t['text_label']}" font-family="{FONT_STACK}" font-size="11.3" font-weight="700" letter-spacing="0.35">REPOS CONTRIBUTED TO</text>

  <!-- Cell 2: repo count & merged count -->
  <text x="342" y="29.5" text-anchor="middle" font-family="{FONT_STACK}" font-size="12.8" xml:space="preserve"><tspan fill="{t['text_primary']}" font-weight="600">{escape(repos_txt)}</tspan><tspan fill="{t['text_secondary']}"> repos</tspan><tspan fill="{t['text_muted']}">&#160;&#160;·&#160;&#160;</tspan><tspan fill="{t['text_primary']}" font-weight="600">{escape(merged_txt)}</tspan><tspan fill="{t['text_secondary']}"> merged</tspan></text>

  <!-- Cell 3: Combined stars -->
  <g transform="translate(478, 18)" fill="{t['gold']}">
    <path d="M6.5 0.8L8.25 4.35L12.17 4.92L9.33 7.68L10.0 11.58L6.5 9.74L3.0 11.58L3.67 7.68L0.83 4.92L4.75 4.35L6.5 0.8Z"/>
  </g>
  <text x="496" y="29.5" font-family="{FONT_STACK}" font-size="12.8" xml:space="preserve"><tspan fill="{t['text_primary']}" font-weight="600">{escape(stars_txt)}</tspan><tspan fill="{t['text_secondary']}"> stars</tspan></text>

  <!-- Cell 4: Combined forks -->
  <g transform="translate(668, 17.5)" stroke="{t['sky']}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" fill="none">
    <circle cx="3.5" cy="3" r="1.9"/>
    <circle cx="10.5" cy="3" r="1.9"/>
    <circle cx="7" cy="12" r="1.9"/>
    <path d="M3.5 4.9V6.2C3.5 7.6 4.6 8.5 7 8.5C9.4 8.5 10.5 7.6 10.5 6.2V4.9"/>
    <path d="M7 8.5V10.1"/>
  </g>
  <text x="687" y="29.5" font-family="{FONT_STACK}" font-size="12.8" xml:space="preserve"><tspan fill="{t['text_primary']}" font-weight="600">{escape(forks_txt)}</tspan><tspan fill="{t['text_secondary']}"> forks</tspan></text>

  <!-- Cell 5: Live cadence indicator -->
  <circle cx="826" cy="25" r="3" fill="{t['emerald']}"/>
  <text x="835" y="29" fill="{t['text_muted']}" font-family="{FONT_STACK}" font-size="11.5" font-weight="500">24h sync</text>'''
    return f"{head}{body}\n{tail}"


def _kaggle_body(
    theme_name: str,
    *,
    entered_count: int,
    ieee_text: str,
    ieee_sub: str,
    quantum_text: str,
    quantum_sub: str,
) -> str:
    t = THEMES[theme_name]
    ieee_len = len(f"IEEE: {ieee_text} {ieee_sub}".strip())
    ieee_fs = "11.0" if ieee_len > 34 else "11.9"
    ieee_sub_fs = "10.2" if ieee_len > 34 else "10.9"

    quantum_len = len(f"Google Quantum AI: {quantum_text} {quantum_sub}".strip())
    quantum_fs = "10.7" if quantum_len > 35 else "11.9"
    quantum_sub_fs = "10.0" if quantum_len > 35 else "10.9"

    ieee_sub_tspan = (
        f'<tspan fill="{t["text_muted"]}" font-size="{ieee_sub_fs}">&#160;{escape(ieee_sub)}</tspan>'
        if ieee_sub
        else ""
    )
    quantum_sub_tspan = (
        f'<tspan fill="{t["text_muted"]}" font-size="{quantum_sub_fs}">&#160;{escape(quantum_sub)}</tspan>'
        if quantum_sub
        else ""
    )

    return f'''
  <!-- Left label: Kaggle mark + Competitions entered -->
  <rect x="16" y="16" width="18" height="18" rx="4.5" fill="{t['kaggle']}" fill-opacity="0.16"/>
  <text x="25" y="29" text-anchor="middle" fill="{t['kaggle']}" font-family="{FONT_STACK}" font-size="11.5" font-weight="800">K</text>
  <text x="41" y="29" font-family="{FONT_STACK}" font-size="11.3" xml:space="preserve"><tspan fill="{t['text_label']}" font-weight="700" letter-spacing="0.35">KAGGLE</tspan><tspan fill="{t['text_muted']}">&#160;·&#160;</tspan><tspan fill="{t['text_secondary']}" font-weight="500">Competitions: </tspan><tspan fill="{t['text_primary']}" font-weight="600">{entered_count}</tspan></text>

  <!-- Button 1: IEEE Big Data public leaderboard -->
  <rect x="249" y="9.5" width="276" height="31" rx="7.5" fill="url(#btnBg)" stroke="url(#btnBorder)" stroke-width="1"/>
  <text x="379" y="29.2" text-anchor="middle" font-family="{FONT_STACK}" font-size="{ieee_fs}" xml:space="preserve"><tspan fill="{t['text_secondary']}" font-weight="500">IEEE: </tspan><tspan fill="{t['text_primary']}" font-weight="600">{escape(ieee_text)}</tspan>{ieee_sub_tspan}</text>
  <path d="M507.5 28.2L514 21.7M509.3 21.7H514V26.4" stroke="{t['btn_icon']}" stroke-opacity="0.85" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/>

  <!-- Button 2: Google Quantum AI public leaderboard -->
  <rect x="535" y="9.5" width="269" height="31" rx="7.5" fill="url(#btnBg)" stroke="url(#btnBorder)" stroke-width="1"/>
  <text x="661.5" y="29.2" text-anchor="middle" font-family="{FONT_STACK}" font-size="{quantum_fs}" xml:space="preserve"><tspan fill="{t['text_secondary']}" font-weight="500">Google Quantum AI: </tspan><tspan fill="{t['text_primary']}" font-weight="600">{escape(quantum_text)}</tspan>{quantum_sub_tspan}</text>
  <path d="M786.5 28.2L793 21.7M788.3 21.7H793V26.4" stroke="{t['btn_icon']}" stroke-opacity="0.85" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/>

  <!-- Right cell: 15m live indicator -->
  <circle cx="826" cy="25" r="3" fill="{t['kaggle']}"/>
  <text x="835" y="29" fill="{t['text_muted']}" font-family="{FONT_STACK}" font-size="11.5" font-weight="500">15m live</text>'''


def render_kaggle_stripe(
    theme_name: str,
    *,
    entered_count: int,
    ieee_text: str,
    ieee_sub: str,
    quantum_text: str,
    quantum_sub: str,
    view_x: int = 0,
    view_w: int = 900,
) -> str:
    t = THEMES[theme_name]
    head, tail = _card_frame(
        theme_name,
        t["kaggle"],
        [242, 809],
        view_x=view_x,
        view_w=view_w,
        include_button_defs=True,
    )
    body = _kaggle_body(
        theme_name,
        entered_count=entered_count,
        ieee_text=ieee_text,
        ieee_sub=ieee_sub,
        quantum_text=quantum_text,
        quantum_sub=quantum_sub,
    )
    return f"{head}{body}\n{tail}"


def render_kaggle_slices(
    theme_name: str,
    *,
    entered_count: int,
    ieee_text: str,
    ieee_sub: str,
    quantum_text: str,
    quantum_sub: str,
) -> dict[str, str]:
    """Render the 4 seamless horizontal slices (`left`, `ieee`, `quantum`, `live`)."""
    out: dict[str, str] = {}
    for slice_name, (vx, vw) in KAGGLE_SLICES.items():
        out[slice_name] = render_kaggle_stripe(
            theme_name,
            entered_count=entered_count,
            ieee_text=ieee_text,
            ieee_sub=ieee_sub,
            quantum_text=quantum_text,
            quantum_sub=quantum_sub,
            view_x=vx,
            view_w=vw,
        )
    return out
