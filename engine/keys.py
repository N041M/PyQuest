"""Raw single-key input -- a stdlib alternative to curses for the one
interactive surface (the launcher menu).

WHY NOT CURSES. curses would give arrow-key menus, but at three costs PyQuest
won't pay: (1) it is NOT stdlib on Windows -- it needs the third-party
`windows-curses`, breaking the no-dependencies rule; (2) it seizes the terminal
with an alternate screen, destroying scrollback -- fatal for a course whose loop
is "read the brief, edit work.py, run a command, scroll back to re-read"; (3) it
is a whole modal runtime for what is, here, a few pickers.

THIS MODULE instead reads keypresses one at a time using only the stdlib:
`termios`+`tty` on POSIX, `msvcrt` on Windows. It owns INPUT only -- output stays
in theme.py/render.py (so the visuals-isolated boundary holds), and it does NOT
switch to an alternate screen: pickers repaint in place with theme.cursor_up /
clear_below, leaving scrollback intact. It is the input-side mirror of inputs.py
(which seeds learner input); this seeds menu navigation.

DEGRADATION is the whole point. supported() is False off a TTY, in a pipe, on a
dumb terminal, or on a platform with neither backend -- and every caller then
falls back to its existing numbered input() prompt. Nothing here is load-bearing
for correctness; it is a nicety that vanishes cleanly when it can't run.

SAFETY. raw() restores the terminal on every exit path, including
KeyboardInterrupt -- the classic curses footgun (a crash stranding the terminal
in raw mode) closed by a finally.

Usage:
    with keys.raw() as live:          # cbreak for the duration, always restored
        if not live:                  # unsupported -> caller uses input()
            ...
        while ...:
            key = keys.read_key()     # UP/DOWN/ENTER/ESC/... or a printable char
or simply:
    i = keys.pick("difficulty", ["easy", "normal", "hard"], index=1)
    if i is None:                     # cancelled OR unsupported -> numbered prompt
        ...
"""

import os
import sys
import contextlib

# Key tokens. Specials are uppercase sentinels; a printable key is returned as
# its own one-character string, so callers can switch on `key == UP` or
# `key == "q"` uniformly.
UP, DOWN, LEFT, RIGHT = "UP", "DOWN", "LEFT", "RIGHT"
ENTER, ESC, BACKSPACE, TAB = "ENTER", "ESC", "BACKSPACE", "TAB"
INTERRUPT = "INTERRUPT"          # Ctrl-C / Ctrl-D / EOF

_ARROWS = {b"A": UP, b"B": DOWN, b"C": RIGHT, b"D": LEFT}
_WIN_ARROWS = {"H": UP, "P": DOWN, "K": LEFT, "M": RIGHT}

# After an ESC byte, wait this long for the rest of an escape sequence (an arrow
# arrives as ESC [ A). Too short and an arrow whose bytes are split across a slow
# link reads as a lone ESC (an accidental cancel); too long and pressing ESC
# itself feels laggy. 50ms is a safe middle that tolerates typical SSH latency.
_ESC_WINDOW = 0.05


def _backend():
    """Which key backend this platform offers: 'posix', 'windows', or None."""
    try:
        import termios, tty                 # noqa: F401  (probe only)
        return "posix"
    except ImportError:
        pass
    try:
        import msvcrt                       # noqa: F401
        return "windows"
    except ImportError:
        return None


def supported():
    """True when keys can be read one at a time here: stdin AND stdout are TTYs
    and a backend exists. False -> the caller keeps its numbered input() path."""
    return (sys.stdin.isatty() and sys.stdout.isatty()
            and _backend() is not None)


@contextlib.contextmanager
def raw():
    """Hold the terminal ready for single-key reads and restore it on every exit
    path (incl. KeyboardInterrupt). On POSIX that means cbreak (no line buffering
    or echo; Ctrl-C still fires); on every backend it also holds auto-wrap OFF so
    one logical line is exactly one screen row -- which is what keeps the
    in-place repaint's row math exact. Yields True when raw input is live, False
    when it isn't (the caller then falls back); unsupported terminals are a clean
    no-op."""
    from .theme import autowrap
    if not supported():
        yield False
        return
    if _backend() == "windows":              # msvcrt: no cbreak switch needed
        sys.stdout.write(autowrap(False)); sys.stdout.flush()
        try:
            yield True
        finally:
            sys.stdout.write(autowrap(True)); sys.stdout.flush()
        return
    import termios, tty
    fd = sys.stdin.fileno()
    saved = termios.tcgetattr(fd)
    try:
        tty.setcbreak(fd)
        sys.stdout.write(autowrap(False)); sys.stdout.flush()
        yield True
    finally:
        sys.stdout.write(autowrap(True)); sys.stdout.flush()
        termios.tcsetattr(fd, termios.TCSADRAIN, saved)


def decode(seq):
    """Map the raw bytes of ONE keypress to a token or character. Pure -- the
    escape-sequence logic is unit-tested without a real terminal (see the
    `key_decode` engine self-test). Handles CSI (ESC [ A) and SS3 (ESC O A)
    arrow forms, Enter, Backspace, Tab, a lone ESC, EOF/Ctrl-C, and printables.
    """
    if seq in (b"", b"\x04", b"\x03"):       # EOF / Ctrl-D / Ctrl-C as a byte
        return INTERRUPT
    if seq in (b"\r", b"\n"):
        return ENTER
    if seq in (b"\x7f", b"\x08"):
        return BACKSPACE
    if seq == b"\t":
        return TAB
    if seq == b"\x1b":                        # ESC with nothing after it
        return ESC
    if seq[:1] == b"\x1b" and len(seq) >= 3 and seq[1:2] in (b"[", b"O"):
        return _ARROWS.get(seq[2:3], ESC)     # arrow, or an unmapped sequence
    try:
        text = seq.decode("utf-8")
    except UnicodeDecodeError:
        return ESC
    return text if len(text) == 1 and text.isprintable() else ESC


def _read_posix():
    import select
    fd = sys.stdin.fileno()
    while True:                               # poll so a SIGWINCH can break in
        if _resized[0]:
            _resized[0] = False
            return _RESIZE
        try:
            ready = select.select([fd], [], [], 0.25)[0]
        except InterruptedError:
            continue                          # a signal woke the wait -> recheck
        if ready:
            break
    ch = os.read(fd, 1)
    if ch != b"\x1b":
        return decode(ch)
    # ESC: read EXACTLY one escape sequence -- never gather past it, or a DOWN
    # immediately followed by ENTER (bytes buffered together as ESC [ B \r) would
    # swallow the \r and the next read_key would block. A lone ESC sends nothing
    # within the window; ESC [ A / ESC O A is the 3-byte arrow form.
    if not select.select([fd], [], [], _ESC_WINDOW)[0]:
        return ESC                            # nothing followed -> a real ESC
    intro = os.read(fd, 1)                     # '[' (CSI) or 'O' (SS3), usually
    if intro not in (b"[", b"O"):
        return decode(b"\x1b" + intro)        # ESC + a plain key
    if not select.select([fd], [], [], _ESC_WINDOW)[0]:
        return ESC                            # malformed ESC [ with no final byte
    return decode(b"\x1b" + intro + os.read(fd, 1))   # the arrow letter


def _read_windows():
    import msvcrt
    ch = msvcrt.getwch()
    if ch in ("\x00", "\xe0"):                # a special key sends a second char
        return _WIN_ARROWS.get(msvcrt.getwch(), ESC)
    if ch in ("\r", "\n"):
        return ENTER
    if ch in ("\x03", "\x04"):
        return INTERRUPT
    if ch == "\x08":
        return BACKSPACE
    if ch == "\x1b":
        return ESC
    return ch if ch.isprintable() else ESC


def read_key():
    """Block for one keypress and return its token (UP/DOWN/.../ENTER/ESC/
    INTERRUPT) or the printable character typed. Call inside raw()."""
    return _read_windows() if _backend() == "windows" else _read_posix()


def _blit(lines, prev_rows):
    """Paint a block, redrawing in place after the first paint. `prev_rows` is
    the row count the previous paint occupied (0 the first time): walk the cursor
    up that many rows, erase to end of screen, then reprint. With auto-wrap held
    OFF (see raw()), each logical line is exactly one screen row, so the count is
    just len(lines) -- exact regardless of terminal width, and so immune to the
    wrap edge cases. clear_below absorbs any change in height between redraws (a
    shorter typed prompt, or a row that re-packed onto fewer lines after a
    resize). Returns the new row count. No alternate screen -> scrollback kept."""
    from .theme import cursor_up, clear_below
    if prev_rows:
        if prev_rows > 1:
            sys.stdout.write(cursor_up(prev_rows - 1))
        sys.stdout.write("\r" + clear_below())
    sys.stdout.write("\n".join(lines))
    sys.stdout.flush()
    return len(lines)


# --- live resize -------------------------------------------------------------
# A terminal resize must re-render: a row re-packs onto a different number of
# lines for the new width. The SIGWINCH handler just sets a flag; the read loop
# turns it into a RESIZE token, which navigate treats as "redraw, consume no
# key". POSIX + main-thread only; elsewhere the picker still works, it just
# won't redraw until the next keypress.
_RESIZE = "RESIZE"
_resized = [False]


def _on_winch(signum, frame):
    _resized[0] = True


def _install_winch():
    import signal
    if _backend() != "posix" or not hasattr(signal, "SIGWINCH"):
        return None
    _resized[0] = False
    try:
        return signal.signal(signal.SIGWINCH, _on_winch)
    except (ValueError, OSError):
        return None                      # not the main thread -> no live redraw


def _restore_winch(previous):
    import signal
    if previous is None or not hasattr(signal, "SIGWINCH"):
        return
    try:
        signal.signal(signal.SIGWINCH, previous)
    except (ValueError, OSError):
        pass


def navigate(render, n, index=0, allow_typing=True, esc_cancels=True):
    """The shared arrow/typing loop behind every menu picker.

    `render(index, buf)` returns the lines to draw (highlight item `index`, show
    the typed `buf`); the line count may vary between calls -- the repaint walks
    the previous count back up and erases to end of screen, so a changing height
    (a resize re-packing a row, a shorter typed prompt) is fine. `n` is the item
    count.
    Returns:
        int   -- Enter on a highlighted item (its index)
        str   -- Enter while typing (the typed text), when allow_typing
        None  -- Esc (if esc_cancels) / EOF, or raw input unsupported
    Ctrl-C propagates as KeyboardInterrupt (the terminal is restored first); the
    caller decides whether that means "back" or "quit". `esc_cancels=False` lets
    a top-level pane ignore Esc (the hub, where 0/quit is the explicit exit).
    """
    if not supported() or n <= 0:
        return None
    index = max(0, min(index, n - 1))
    buf, prev_rows = "", 0
    winch = _install_winch()
    try:
        with raw() as live:
            if not live:
                return None
            while True:
                prev_rows = _blit(render(index, buf), prev_rows)
                key = read_key()
                if key == _RESIZE:                # terminal resized -> just redraw
                    continue
                if key in (UP, LEFT):             # LEFT/RIGHT too, for a row
                    buf, index = "", (index - 1) % n
                elif key in (DOWN, RIGHT):
                    buf, index = "", (index + 1) % n
                elif key == ENTER:
                    sys.stdout.write("\n")
                    return buf if (allow_typing and buf) else index
                elif key == INTERRUPT or (key == ESC and esc_cancels):
                    sys.stdout.write("\n")
                    return None
                elif allow_typing and key == BACKSPACE:
                    buf = buf[:-1]
                elif (allow_typing and isinstance(key, str) and len(key) == 1
                        and key.isprintable()):       # a real char, not a UP/ESC
                    buf += key
                elif not allow_typing and key == "q":
                    sys.stdout.write("\n")
                    return None
                # any other key: ignore and redraw
    finally:
        _restore_winch(winch)


def pick(title, options, index=0, allow_typing=False, max_rows=None):
    """Flat-list selection over `options` (display strings), built on navigate.
    Returns the chosen index, the typed string (when allow_typing), or None
    (cancelled / unsupported) -- so callers keep a typed prompt as the fallback:

        choice = keys.pick(...)
        if choice is None:
            ...typed input() prompt...

    max_rows windows a long list (e.g. the 98-puzzle level picker) around the
    selection. Output goes through theme/render; no alternate screen.
    """
    from .theme import paint, CUR
    from .render import PAD
    if not (supported() and options):
        return None
    n = len(options)
    view = min(max_rows or n, n)
    state = {"top": 0}

    def render(idx, buf):
        top = state["top"]
        if idx < top:
            top = idx
        elif idx >= top + view:
            top = idx - view + 1
        state["top"] = top = max(0, min(top, n - view))
        lines = []
        for r in range(top, top + view):
            on = r == idx
            mark = paint(CUR, "bcyan", "bold") if on else " "
            lines.append("%s%s %s" % (PAD, mark, paint(
                options[r], "byellow" if on else "white", "bold")))
        if allow_typing and buf:
            lines.append(PAD + paint("> ", "cyan", "bold") + buf)
        else:
            tail = ["arrows move", "Enter select"]
            if allow_typing:
                tail.append("type to enter one")
            tail.append("Esc back")
            more = "   %d of %d" % (idx + 1, n) if n > view else ""
            lines.append(PAD + paint(" · ".join(tail) + more, "gray"))
        return lines

    try:
        return navigate(render, n, index=index, allow_typing=allow_typing)
    except KeyboardInterrupt:
        return None
