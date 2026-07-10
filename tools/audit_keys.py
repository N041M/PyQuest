"""Interactive-layer self-test (`python3 tools/audit.py --keys`).

The one part of PyQuest the rest of the audit can't reach: engine/keys.py and the
arrow-driven surfaces built on it (the menu hub, the play cockpit). They need a
real terminal, so this drives a PSEUDO-terminal -- os.openpty() is a TTY without
a terminal, and ioctl(TIOCSWINSZ) lets us script the exact size that breaks
things (a short Codespaces panel). A drainer/writer thread feeds real keystrokes
through it; a SIGALRM guards against hangs. We assert on RETURNED values, so this
proves the real raw-mode / decode / navigate / _fits / fallback paths behave --
it cannot judge whether a screen *looks* right (only your eyes can do that).

POSIX only (needs a pty + termios); a clean skip elsewhere.
"""

import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)


def _supported_platform():
    try:
        import termios, fcntl, pty            # noqa: F401
        return hasattr(__import__("signal"), "SIGALRM")
    except ImportError:
        return False


def keys_selftest():
    if not _supported_platform():
        print("keys self-test: skipped (needs a POSIX pty + termios)")
        return 0

    import termios
    import struct
    import fcntl
    import signal
    import threading
    import time
    import tempfile
    import shutil
    from engine import keys
    import engine.commands.menu as menu
    import engine.commands.cards as cards

    results = []

    def case(label, fn):
        try:
            fn()
        except AssertionError as e:
            results.append((label, "FAIL: %s" % e))
        except Exception as e:
            results.append((label, "FAIL: %s: %s" % (type(e).__name__, e)))
        else:
            results.append((label, "ok"))

    def set_winsize(fd, rows, cols):
        fcntl.ioctl(fd, termios.TIOCSWINSZ, struct.pack("HHHH", rows, cols, 0, 0))

    def on_pty(rows, cols, fn, actions=(), timeout=5):
        """Run fn() with stdin/stdout on a fresh `rows`x`cols` pty while a thread
        drains the output and performs `actions` -- each a (delay_s, payload),
        payload being bytes to send as keystrokes or a callable to invoke (e.g.
        a resize). Returns fn()'s value; raises on timeout. Always restores fds."""
        master, slave = os.openpty()
        set_winsize(slave, rows, cols)
        saved0, saved1 = os.dup(0), os.dup(1)
        os.dup2(slave, 0)
        os.dup2(slave, 1)
        os.set_blocking(master, False)
        stop = threading.Event()

        def driver():
            t0, i, todo = time.time(), 0, list(actions)
            while not stop.is_set() and time.time() - t0 < timeout + 1:
                try:
                    os.read(master, 8192)            # drain, so slave never blocks
                except (BlockingIOError, OSError):
                    pass
                if i < len(todo) and time.time() - t0 >= todo[i][0]:
                    payload = todo[i][1]
                    if callable(payload):
                        payload()
                    else:
                        os.write(master, payload)
                    i += 1
                time.sleep(0.01)

        th = threading.Thread(target=driver, daemon=True)
        th.start()
        old = signal.signal(signal.SIGALRM,
                            lambda *a: (_ for _ in ()).throw(TimeoutError("hung")))
        signal.setitimer(signal.ITIMER_REAL, timeout)
        try:
            return fn()
        finally:
            signal.setitimer(signal.ITIMER_REAL, 0)
            signal.signal(signal.SIGALRM, old)
            stop.set()
            os.dup2(saved0, 0)
            os.dup2(saved1, 1)
            for fd in (saved0, saved1, master, slave):
                try:
                    os.close(fd)
                except OSError:
                    pass

    # a trivially navigable render: one row, highlight ignored
    def row(i, b):
        return ["item %d" % i, "hint"]

    # ---- pure / non-pty ----------------------------------------------------
    def t_decode():
        d = keys.decode
        assert d(b"\x1b[A") == keys.UP and d(b"\x1bOA") == keys.UP
        assert d(b"\x1b[B") == keys.DOWN and d(b"\x1b[C") == keys.RIGHT
        assert d(b"\r") == keys.ENTER and d(b"\x7f") == keys.BACKSPACE
        assert d(b"\x1b") == keys.ESC and d(b"") == keys.INTERRUPT
        assert d(b"q") == "q" and d(b"\x1b[Z") == keys.ESC

    def t_supported_off_pipe():
        # under the audit's pipe, stdout is not a tty
        assert keys.supported() is False, "claimed raw input under a pipe"

    # ---- real pty ----------------------------------------------------------
    def t_supported_on_pty():
        assert on_pty(24, 80, keys.supported) is True

    def t_raw_restores():
        PENDIN = 0x20000000

        def check():
            before = termios.tcgetattr(0)
            with keys.raw() as live:
                assert live is True
                assert not (termios.tcgetattr(0)[3] & termios.ICANON)  # cbreak
            after = termios.tcgetattr(0)
            assert after[3] & termios.ICANON                          # restored
            raised = False
            try:
                with keys.raw():
                    raise ValueError("boom")
            except ValueError:
                raised = True
            post = termios.tcgetattr(0)
            ok = (raised and (post[3] & termios.ICANON)
                  and (before[3] | PENDIN) == (post[3] | PENDIN))     # ignore PENDIN
            assert ok, "raw() did not restore termios (incl. on exception)"
        on_pty(24, 80, check)

    def t_read_key_pty():
        def read_one():                          # read_key must run inside raw()
            with keys.raw():
                return keys.read_key()
        for raw_bytes, want in [(b"\x1b[B", keys.DOWN), (b"\x1bOA", keys.UP),
                                (b"\x1b", keys.ESC), (b"k", "k")]:
            got = on_pty(24, 80, read_one, [(0.3, raw_bytes)])
            assert got == want, "read_key(%r) -> %r, want %r" % (
                raw_bytes, got, want)

    def t_navigate_returns():
        down_enter = on_pty(24, 80, lambda: keys.navigate(row, 3),
                            [(0.3, b"\x1b[B"), (0.55, b"\r")])
        assert down_enter == 1, "navigate DOWN,ENTER -> %r" % down_enter
        typed = on_pty(24, 80, lambda: keys.navigate(row, 3, allow_typing=True),
                       [(0.3, b"hi"), (0.55, b"\r")])
        assert typed == "hi", "navigate type 'hi' -> %r" % typed
        cancelled = on_pty(24, 80, lambda: keys.navigate(row, 3),
                           [(0.3, b"\x1b")])
        assert cancelled is None, "navigate ESC -> %r" % cancelled

    def t_fits_by_winsize():
        short = on_pty(10, 80, lambda: menu._fits(21))
        tall = on_pty(40, 120, lambda: menu._fits(21))
        assert short is False and tall is True, "short=%r tall=%r" % (short, tall)

    def t_menu_compact_on_short():
        orig = menu.current_puzzle
        menu.current_puzzle = lambda *a, **k: {"id": "1.1", "meta": {"title": "x"}}
        prog = {"completed": ["1.1"], "mode": "normal"}
        puz = [{"id": "1.1"}] * 98
        try:                                          # 10 rows -> compact path
            out = on_pty(10, 100, lambda: menu._menu_input(puz, {"1.1": puz[0]},
                                                           prog),
                         [(0.4, b"\x1b[B"), (0.65, b"\r")])
        finally:
            menu.current_puzzle = orig
        assert out == "2", "compact menu DOWN,ENTER -> %r (want '2')" % out

    def t_menu_switch_propagates():
        # A profile switched INSIDE the menu must propagate out of cmd_menu (via
        # dispatch) so _play/check run against the new profile, not the pre-menu
        # one. Regression for the card-vs-checker desync. In a sandboxed users/,
        # 'alice' sits on a later puzzle; at the hub we type 'user bob' to switch
        # (creating bob fresh, current = the first puzzle) then '0' to leave. The
        # prog dispatch returns must be bob's (first puzzle), not alice's.
        import json
        import engine.config as cfg
        import engine.state as state
        from engine.content import discover
        from engine.app import dispatch
        saved = (cfg.USERS_DIR, cfg.SETTINGS_PATH, cfg._LEGACY_SETTINGS,
                 state.USERS_DIR)
        sand = tempfile.mkdtemp(prefix="pyquest_keystest_")
        cfg.USERS_DIR = os.path.join(sand, "users")
        cfg.SETTINGS_PATH = os.path.join(cfg.USERS_DIR, "settings.json")
        cfg._LEGACY_SETTINGS = os.path.join(sand, "nope.json")
        state.USERS_DIR = cfg.USERS_DIR
        try:
            os.makedirs(cfg.USERS_DIR, exist_ok=True)
            puzzles = discover()
            by_id = {p["id"]: p for p in puzzles}
            first, later = puzzles[0]["id"], puzzles[7]["id"]

            def setj(path, obj):
                with open(path, "w") as f:
                    json.dump(obj, f)
            setj(cfg.SETTINGS_PATH, {"user": "alice"})
            state.ensure_user("alice")
            ap = state.default_progress(puzzles)
            ap["current"], ap["active"], ap["highest"] = later, True, 99
            setj(state.progress_path("alice"), ap)
            setj(os.path.join(cfg.USERS_DIR, "alice", "answers.json"), {})
            prog, _ = state.load_progress(puzzles)
            out = on_pty(24, 100,
                         lambda: dispatch(["menu"], puzzles, by_id, prog),
                         [(0.3, b"user bob\r"), (0.7, b"0\r")])
            assert state.current_user() == "bob", \
                "switch didn't persist: %s" % state.current_user()
            assert isinstance(out, dict) and out.get("current") == first, \
                "menu returned stale prog: current=%r (want %r)" % (
                    (out.get("current") if isinstance(out, dict) else out), first)
        finally:
            (cfg.USERS_DIR, cfg.SETTINGS_PATH, cfg._LEGACY_SETTINGS,
             state.USERS_DIR) = saved
            shutil.rmtree(sand, ignore_errors=True)

    def t_shortcuts_pane_arrow():
        # The shortcuts settings pane must be arrow-navigable like its siblings,
        # not a raw input() prompt: on a key-capable TTY it drives keys.pick, so
        # Esc backs out cleanly. (The old input()-only version would block on an
        # Esc that never sends a newline -- caught here as a timeout.)
        out = on_pty(24, 100, menu._menu_shortcuts,
                     [(0.3, b"\x1b[B"), (0.5, b"\x1b[B"), (0.7, b"\x1b")])
        assert out is None, "shortcuts pane DOWN,DOWN,ESC -> %r (want None)" % out

    def t_cockpit_nav_select():
        prog = {"active": True, "completed": [], "mode": "normal"}
        cur = {"id": "1.1", "index": 0}
        puz = [{"id": "1.1", "index": 0}, {"id": "1.2", "index": 1}]
        # 140 cols -> the row fits on one line; 40 cols -> it stacks the clusters.
        # The index->verb mapping (and the repaint) must survive both packings.
        for cols in (140, 40):
            out = on_pty(24, cols, lambda: cards.nav_select(prog, cur, puz),
                         [(0.3, b"\x1b[C"), (0.55, b"\r")])   # RIGHT -> verbs[1]
            assert out == "hint", "cockpit (%d cols) RIGHT,ENTER -> %r" % (cols, out)

    def t_resize_redraws():
        # resize mid-navigation (winsize change + SIGWINCH), then finish the pick;
        # the RESIZE token must be consumed as a redraw, not break navigation
        def resize_then_nav(slave_holder):
            def do_resize():
                os.kill(os.getpid(), signal.SIGWINCH)
            out = on_pty(24, 120, lambda: keys.navigate(row, 3),
                         [(0.3, do_resize), (0.5, b"\x1b[B"), (0.75, b"\r")])
            return out
        out = resize_then_nav(None)
        assert out == 1, "navigate survived a resize -> %r (want 1)" % out

    for fn in (t_decode, t_supported_off_pipe, t_supported_on_pty, t_raw_restores,
               t_read_key_pty, t_navigate_returns, t_fits_by_winsize,
               t_menu_compact_on_short, t_menu_switch_propagates,
               t_shortcuts_pane_arrow, t_cockpit_nav_select, t_resize_redraws):
        case(fn.__name__[2:], fn)

    bad = 0
    for label, verdict in results:
        print("%-26s %s" % (label, verdict))
        if verdict != "ok":
            bad += 1
    print("\n%d/%d keys self-tests pass" % (len(results) - bad, len(results)))
    return 1 if bad else 0
