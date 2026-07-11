"""Drawing primitives. The only place (with theme.py) that knows box characters
and layout math. Everything else builds screens from these.
"""

import os
import textwrap

from .config import WIDTH
from .theme import (paint, paint_code, hyperlink,
                    OK, NO, CUR, DOT, ARROW, STAR, BOLT, RETRY,
                    LOGO, LOGO_RAMP, id_art)
from .i18n import t

PAD = "   "          # standard content indent


# Verbs with no bare shell shortcut (see shell/pyquest.*): `export`/`import`
# would collide with the shell's own `export` built-in, so they stay reachable
# only through the umbrella `start export`. cli() must show them that way -- a
# bare `export` the shell wouldn't define would be a dead instruction.
UMBRELLA_ONLY = ("export", "import")


def cli(verb=""):
    """Render a command the way the learner invokes it.

    If the shell shortcuts are installed (PYQUEST_SHELL=1), show the bare verb
    like `check`; otherwise show the full `python3 start.py check`. Verbs with no
    bare shortcut fall back to the umbrella form (`start export`) so whatever we
    print is something the learner can actually run.
    """
    if os.environ.get("PYQUEST_SHELL"):
        if not verb:
            return "start"
        return "start " + verb if verb.split()[0] in UMBRELLA_ONLY else verb
    return ("python3 start.py " + verb).strip()


def label(text):
    return paint(text, "cyan", "bold")


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


def section(title, color="magenta"):
    """A heavier banner that groups chapters under a curriculum category --
    ═══ ADVANCED ═══════ -- a step above the per-chapter `header`."""
    label = " %s " % title.upper()
    tail = WIDTH - len(PAD) - 3 - len(label)
    return paint("%s═══%s%s" % (PAD, label, "═" * max(0, tail)), color, "bold")


def wrap(text, width=None):
    return textwrap.wrap(text, width or (WIDTH - len(PAD) - 1)) or [""]


def field(label_text, value, lblcolor="cyan"):
    return "%s%s  %s" % (PAD, paint(label_text.ljust(6), lblcolor, "bold"), value)


def swatch():
    """A six-block color strip -- the active palette at a glance."""
    return "".join(paint("██", r) for r in
                   ("cyan", "byellow", "green", "yellow", "red", "magenta"))


def bar(done, total, width=26):
    if total <= 0:
        return paint("░" * width, "gray")
    filled = max(0, min(width, int(round(width * done / total))))
    color = "green" if done >= total else "bcyan"
    meter = paint("█" * filled, color) + paint("░" * (width - filled), "gray")
    return "%s  %s" % (meter, paint("%d / %d" % (done, total), "bold"))


def sparkline(values):
    """One row of block glyphs scaled to the series' own max; a zero renders
    as a dim dot so quiet days read as gaps, not noise. Empty-safe."""
    ramp = "▁▂▃▄▅▆▇█"
    top = max(values) if values else 0
    if top <= 0:
        return paint(DOT * len(values), "gray")
    out = []
    for v in values:
        if v <= 0:
            out.append(paint(DOT, "gray"))
        else:
            i = max(0, min(len(ramp) - 1, (v * len(ramp) - 1) // top))
            out.append(paint(ramp[i], "bcyan"))
    return "".join(out)


def indent(text, prefix="  "):
    return "\n".join(prefix + ln for ln in text.split("\n"))


def quote_block(value, mark=None):
    """An indented `| `-quoted block. `mark` points an arrow at one line (the
    checker's first-differing-line) -- past-the-end marks a row the block is
    MISSING, drawn as an empty marked line so the gap itself is visible."""
    text = value if isinstance(value, str) else repr(value)
    lines = text.split("\n") if text != "" else [""]
    if mark is not None and mark >= len(lines):
        lines = lines + [""]
        mark = len(lines) - 1
    out = []
    for i, ln in enumerate(lines):
        lead = "  %s | " % paint(CUR, "byellow", "bold") if i == mark \
            else "    | "
        out.append(lead + ln)
    return "\n".join(out)


def pane_open(title, mode, done, total, color="cyan"):
    """The shared opener every sub-pane prints: a titled header rule above a
    `mode + progress` line. This is the menu's gold-standard combo lifted into
    one primitive so map/goto/hint/solution all frame themselves identically."""
    meter = "%s%s     %s" % (PAD, paint(mode + " " + t("ui.mode", "mode"),
                                        "magenta", "bold"),
                             bar(done, total, WIDTH - 24))
    return header(title, color) + "\n\n" + meter


def nav_row(primary, clusters):
    """A horizontal navigation strip: a highlighted primary-action chip followed
    by dim, ·-separated clusters of secondary verbs, the clusters set apart by
    whitespace. `primary` is a verb label (or None); `clusters` is a list of
    label-lists. The registry-aware selection lives in commands/cards.py."""
    parts = []
    if primary:
        parts.append(paint("[ %s ]" % primary, "byellow", "bold"))
    for labels in clusters:
        if labels:
            parts.append(paint(" · ".join(labels), "gray"))
    return PAD + "   ".join(parts)


def legend():
    """The shared status-marker key, reused by map and the goto picker."""
    return PAD + paint(t("ui.legend", "%s done   %s here   %s to do")
                       % (OK, CUR, DOT), "gray")
