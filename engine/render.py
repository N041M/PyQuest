"""Drawing primitives. The only place (with theme.py) that knows box characters
and layout math. Everything else builds screens from these.
"""

import os
import textwrap

from .config import WIDTH
from .theme import (paint, paint_code,
                    OK, NO, CUR, DOT, ARROW, STAR, LOGO, LOGO_RAMP, id_art)

PAD = "   "          # standard content indent


def cli(verb=""):
    """Render a command the way the learner invokes it.

    If the shell shortcuts are installed (PYQUEST_SHELL=1), show the bare verb
    like `check`; otherwise show the full `python3 start.py check`.
    """
    if os.environ.get("PYQUEST_SHELL"):
        return verb if verb else "start"
    return ("python3 start.py " + verb).strip()


def label(text):
    return paint(text, "cyan", "bold")


def rule(color="gray", width=WIDTH):
    return paint("─" * width, color)


def _center(text, inner):
    gap = inner - len(text)
    left = gap // 2
    return " " * left + text + " " * (gap - left)


def deco_border(left, right, inner, orn=" ✦ "):
    """An edge with a centered ornament:  ╔════ ✦ ════╗"""
    chars = list("═" * inner)
    start = (inner - len(orn)) // 2
    for i, ch in enumerate(orn):
        chars[start + i] = ch
    return left + "".join(chars) + right


def box(title, color="cyan", tall=False):
    """A framed banner with ornamented edges. `tall` adds vertical room."""
    inner = WIDTH - 2
    body = ([" " * inner] if tall else []) + [_center(title, inner)] \
        + ([" " * inner] if tall else [])
    lines = [deco_border("╔", "╗", inner)] \
        + ["║" + b + "║" for b in body] + [deco_border("╚", "╝", inner)]
    return "\n".join(paint(s, color, "bold") for s in lines)


def banner(title, color="cyan"):
    return box(title, color)


def bigbox(art_lines, border="cyan", ramp=None):
    """Frame ASCII art full width with ornaments and an optional color ramp."""
    inner = WIDTH - 2
    edge = lambda l, r: paint(deco_border(l, r, inner), border, "bold")
    corners = paint("║", border, "bold") + paint(
        " " + DOT + " " * (inner - 4) + DOT + " ", border) \
        + paint("║", border, "bold")
    out = [edge("╔", "╗"), corners]
    for i, ln in enumerate(art_lines):
        centered = _center(ln, inner)
        body = paint_code(centered, ramp[i % len(ramp)]) if ramp \
            else paint(centered, border, "bold")
        out.append(paint("║", border, "bold") + body
                   + paint("║", border, "bold"))
    out += [corners, edge("╚", "╝")]
    return "\n".join(out)


def wordmark(color="cyan"):
    """The PyQuest banner: gradient ASCII-art logo if it fits, else a title."""
    if WIDTH - 2 >= max(len(ln) for ln in LOGO):
        return bigbox(LOGO, color, ramp=LOGO_RAMP)
    return box("P Y Q U E S T", color, tall=True)


def id_banner(pid, color="cyan"):
    """A framed, gradient ASCII rendering of a puzzle id (e.g. 2.4).

    Shown when arriving at a new quiz. Falls back to a plain box if the art is
    wider than the terminal.
    """
    art = id_art(pid)
    if WIDTH - 2 >= max(len(ln) for ln in art):
        return bigbox(art, color, ramp=LOGO_RAMP)
    return box(pid, color, tall=True)


def header(title, color="cyan"):
    """A light inline section header:  -- TITLE --------------------"""
    tail = WIDTH - len(PAD) - 3 - len(title) - 1
    return paint("%s── %s %s" % (PAD, title, "─" * max(0, tail)), color, "bold")


def wrap(text, width=None):
    return textwrap.wrap(text, width or (WIDTH - len(PAD) - 1)) or [""]


def field(label_text, value, lblcolor="cyan"):
    return "%s%s  %s" % (PAD, paint(label_text.ljust(6), lblcolor, "bold"), value)


def bar(done, total, width=26):
    if total <= 0:
        return paint("░" * width, "gray")
    filled = max(0, min(width, int(round(width * done / total))))
    color = "green" if done >= total else "bcyan"
    meter = paint("█" * filled, color) + paint("░" * (width - filled), "gray")
    return "%s  %s" % (meter, paint("%d / %d" % (done, total), "bold"))


def indent(text, prefix="  "):
    return "\n".join(prefix + ln for ln in text.split("\n"))


def quote_block(value):
    text = value if isinstance(value, str) else repr(value)
    lines = text.split("\n") if text != "" else [""]
    return "\n".join("    | " + ln for ln in lines)
