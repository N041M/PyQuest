"""The visual identity: palette, glyphs, logo, paint(). The swappable look.

To restyle PyQuest, edit this file (and render.py). No other module contains a
colour code or a box character.
"""

import sys
import os


def _supports_color():
    return (sys.stdout.isatty()
            and os.environ.get("NO_COLOR") is None
            and os.environ.get("TERM") not in (None, "dumb"))


COLOR = _supports_color()


def _fg(n):
    return "\033[38;5;%dm" % n


# Selectable 256-color palettes. Same role names everywhere; switching a theme
# retunes every hue at once. Roles:
#   cyan = structure (frames/headers/labels)   byellow = highlight (ids/titles)
#   bcyan = "you are here" marker               green/red = success/failure
#   yellow = hints   magenta = mode/solution    blue = file paths   gray = dim
_ROLES = ("red", "green", "yellow", "blue", "magenta", "cyan", "white",
          "gray", "bgreen", "bcyan", "byellow", "bred")
THEMES = {
    "neon": {"red": 204, "green": 48, "yellow": 214, "blue": 75,
             "magenta": 177, "cyan": 141, "white": 231, "gray": 244,
             "bgreen": 84, "bcyan": 51, "byellow": 212, "bred": 210,
             "ramp": [211, 177, 141, 105, 69, 45]},
    "amber": {"red": 203, "green": 150, "yellow": 220, "blue": 180,
              "magenta": 209, "cyan": 214, "white": 230, "gray": 244,
              "bgreen": 156, "bcyan": 223, "byellow": 216, "bred": 209,
              "ramp": [229, 223, 216, 214, 208, 202]},
    "forest": {"red": 203, "green": 42, "yellow": 185, "blue": 109,
               "magenta": 114, "cyan": 35, "white": 194, "gray": 240,
               "bgreen": 120, "bcyan": 85, "byellow": 149, "bred": 174,
               "ramp": [120, 84, 78, 42, 36, 30]},
    "mono": {"red": 248, "green": 250, "yellow": 253, "blue": 249,
             "magenta": 250, "cyan": 250, "white": 255, "gray": 243,
             "bgreen": 252, "bcyan": 254, "byellow": 255, "bred": 248,
             "ramp": [255, 253, 251, 249, 247, 245]},
}


def _clamp(n):
    return max(0, min(255, int(n)))


def load_presets():
    """Read user-made JSON theme presets from the themes/ folder.

    Each themes/<name>.json maps any of the role names below to a 256-colour
    code (0-255), plus an optional "ramp" of 6 codes for the logo gradient.
    Anything you leave out inherits from the built-in `neon` theme, so a preset
    can be as small as {"cyan": 39, "ramp": [45,39,33,27,75,81]}.
    """
    import json
    from .config import THEMES_DIR
    presets = {}
    if not os.path.isdir(THEMES_DIR):
        return presets
    base = THEMES["neon"]
    for fn in sorted(os.listdir(THEMES_DIR)):
        if not fn.endswith(".json"):
            continue
        try:
            with open(os.path.join(THEMES_DIR, fn)) as f:
                data = json.load(f)
        except (OSError, ValueError):
            continue                       # skip malformed files quietly
        if not isinstance(data, dict):
            continue
        pal = {r: int(base[r]) for r in _ROLES}
        for r in _ROLES:
            if isinstance(data.get(r), (int, float)):
                pal[r] = _clamp(data[r])
        ramp = data.get("ramp")
        if (isinstance(ramp, list) and ramp
                and all(isinstance(x, (int, float)) for x in ramp)):
            pal["ramp"] = [_clamp(x) for x in ramp]
        else:
            pal["ramp"] = list(base["ramp"])
        presets[fn[:-5]] = pal             # filename (sans .json) is the name
    return presets


THEMES.update(load_presets())              # JSON presets extend/override builtins
THEME_NAMES = tuple(THEMES)

ANSI = {"reset": "\033[0m", "bold": "\033[1m", "dim": "\033[2m"}
LOGO_RAMP = []                       # filled by apply_theme()
OK, NO, CUR, DOT, ARROW, STAR = "✓", "✗", "▸", "·", "→", "✦"


def apply_theme(name):
    """Switch palette in place so already-imported references update live."""
    pal = THEMES.get(name) or THEMES["neon"]
    for role in _ROLES:
        ANSI[role] = _fg(pal[role])
    LOGO_RAMP[:] = pal["ramp"]
    return name in THEMES


def _active_theme():
    try:
        from .config import load_settings
        return load_settings().get("theme", "neon")
    except Exception:
        return "neon"


apply_theme(_active_theme())

# ANSI Shadow wordmark for the title banners.
LOGO = [
    "██████╗ ██╗   ██╗ ██████╗ ██╗   ██╗███████╗███████╗████████╗",
    "██╔══██╗╚██╗ ██╔╝██╔═══██╗██║   ██║██╔════╝██╔════╝╚══██╔══╝",
    "██████╔╝ ╚████╔╝ ██║   ██║██║   ██║█████╗  ███████╗   ██║   ",
    "██╔═══╝   ╚██╔╝  ██║▄▄ ██║██║   ██║██╔══╝  ╚════██║   ██║   ",
    "██║        ██║   ╚██████╔╝╚██████╔╝███████╗███████║   ██║   ",
    "╚═╝        ╚═╝    ╚══▀▀═╝  ╚═════╝ ╚══════╝╚══════╝   ╚═╝   ",
]
# pad to a uniform width so trimmed trailing spaces can't ragged the border
_LOGO_W = max(len(ln) for ln in LOGO)
LOGO = [ln.ljust(_LOGO_W) for ln in LOGO]

# (LOGO_RAMP is defined above and set by apply_theme(); the per-theme gradient.)

# ANSI Shadow digits (+ '.') for the big per-puzzle id banner.
DIGITS = {
    "0": [" ██████╗ ", "██╔═████╗", "██║██╔██║", "████╔╝██║", "╚██████╔╝",
          " ╚═════╝ "],
    "1": ["  ██╗", " ███║", " ╚██║", "  ██║", "  ██║", "  ╚═╝"],
    "2": ["██████╗ ", "╚════██╗", " █████╔╝", "██╔═══╝ ", "███████╗",
          "╚══════╝"],
    "3": ["██████╗ ", "╚════██╗", " █████╔╝", " ╚═══██╗", "██████╔╝",
          "╚═════╝ "],
    "4": ["██╗  ██╗", "██║  ██║", "███████║", "╚════██║", "     ██║",
          "     ╚═╝"],
    "5": ["███████╗", "██╔════╝", "███████╗", "╚════██║", "███████║",
          "╚══════╝"],
    "6": [" ██████╗ ", "██╔════╝ ", "███████╗ ", "██╔═══██╗", "╚██████╔╝",
          " ╚═════╝ "],
    "7": ["███████╗", "╚════██║", "    ██╔╝", "   ██╔╝ ", "   ██║  ",
          "   ╚═╝  "],
    "8": [" █████╗ ", "██╔══██╗", "╚█████╔╝", "██╔══██╗", "╚█████╔╝",
          " ╚════╝ "],
    "9": [" █████╗ ", "██╔══██╗", "╚██████║", " ╚═══██║", " █████╔╝",
          " ╚════╝ "],
    ".": ["   ", "   ", "   ", "   ", "██╗", "╚═╝"],
}


def id_art(text):
    """Render an id like '2.4' as 6 rows of ANSI-Shadow digits (uniform width)."""
    rows = ["", "", "", "", "", ""]
    for ch in text:
        glyph = DIGITS.get(ch)
        if glyph is None:
            continue
        w = max(len(r) for r in glyph)
        for i in range(6):
            rows[i] += glyph[i].ljust(w) + " "
    return rows


def paint(text, *names):
    if not COLOR or not names:
        return text
    return "".join(ANSI[n] for n in names) + text + ANSI["reset"]


def paint_code(text, code, bold=True):
    if not COLOR:
        return text
    return ("\033[1m" if bold else "") + _fg(code) + text + ANSI["reset"]
