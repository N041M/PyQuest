"""The interactive launcher menu -- the one allowed interactive surface (see
docs/ARCHITECTURE.md sec 3, invariant 8a). The puzzle-solving loop stays single-shot
commands; this sits on top of the verbs, composing cards + profiles + shortcuts.
"""

import sys

from ..config import load_settings
from ..state import current_puzzle, activate, load_answers, current_user
from ..render import paint, wordmark, header, cli, PAD
from .cards import print_current_card, _goto_list, _resolve_goto, _jump
from .profiles import cmd_theme, cmd_user
from .shortcuts import (_is_persistent, _disclaimer, _local_source_cmd,
                        cmd_setup_persist, cmd_uninstall)


def cmd_menu(puzzles, by_id, prog):
    """Reach the main menu from anywhere -- an alias for `begin`, so a learner
    mid-puzzle can always type `menu` to get back to start/level/theme/etc."""
    return cmd_begin(puzzles, by_id, prog)


def cmd_begin(puzzles, by_id, prog):
    if not sys.stdin.isatty():
        print(wordmark("cyan"))
        _menu_options(puzzles, by_id, prog)
        print(PAD + paint("(run this in a terminal to choose)", "gray"))
        return
    print(wordmark("cyan"))
    while True:
        _menu_options(puzzles, by_id, prog)
        try:
            choice = input(PAD + paint("> ", "cyan", "bold")).strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("")
            return
        if choice in ("1", "start", "continue", "play", ""):
            cur = current_puzzle(prog, by_id, puzzles)
            activate(prog, cur, load_answers())     # load the puzzle into work.py
            print("")
            print_current_card(prog, cur, show_pointer=(prog["mode"] == "easy"),
                               arriving=True)
            return
        elif choice in ("2", "level", "select", "goto"):
            _menu_level(puzzles, by_id, prog)
        elif choice in ("3", "theme"):
            _menu_theme()
        elif choice in ("4", "users", "user"):
            prog = _menu_users(puzzles, by_id, prog)
        elif choice in ("5", "shortcuts", "short"):
            _menu_shortcuts()
        elif choice in ("6", "q", "quit", "exit"):
            print(PAD + paint("see you in the terminal -- solve with  "
                              + cli("check"), "gray"))
            return
        else:
            print(PAD + paint("type a number 1-6.", "yellow"))
        print("")


def _menu_options(puzzles, by_id, prog):
    done, total = len(prog["completed"]), len(puzzles)
    cur = current_puzzle(prog, by_id, puzzles)
    print("")
    print(header("main menu", "cyan"))
    print("")

    def item(n, lbl, note=""):
        print(PAD + paint(" %s " % n, "byellow", "bold") + "  "
              + paint(lbl.ljust(15), "white", "bold") + paint(note, "gray"))

    here = "%s · %s · %d/%d" % (cur["id"] if cur else "-", prog["mode"],
                                done, total)
    item("1", "start", here)
    item("2", "select level", "jump to any puzzle")
    item("3", "theme", load_settings().get("theme", "neon"))
    item("4", "users", current_user())
    item("5", "shortcuts", "persistent: %s"
         % ("on" if _is_persistent() else "off"))
    item("6", "quit")
    print("")


def _menu_level(puzzles, by_id, prog):
    _goto_list(puzzles, by_id, prog, footer=False)
    try:
        pid = input(PAD + paint("id (blank = cancel) > ", "cyan", "bold")).strip()
    except (EOFError, KeyboardInterrupt):
        return
    if not pid:
        return
    target = _resolve_goto(pid, puzzles, by_id, prog)
    if target is None:
        print(PAD + paint("no puzzle '%s'." % pid, "yellow"))
        return
    # same lock rules as goto -- the menu must not be a side door
    _jump(target, puzzles, by_id, prog)


def _menu_theme():
    # Stay in the theme menu until the user enters a blank line (cancel).
    while True:
        cmd_theme("")                               # show the picker
        try:
            c = input(PAD + paint("theme name (blank = back) > ", "cyan",
                                  "bold")).strip().lower()
        except (EOFError, KeyboardInterrupt):
            return
        if not c:
            return
        if c.startswith("theme "):                  # forgive "theme ocean"
            c = c[6:].strip()
        cmd_theme(c)                                # applies + persists live


def _menu_users(puzzles, by_id, prog):
    # Stay in the users menu until a blank line (cancel).
    while True:
        cmd_user("", puzzles, by_id, prog)          # list users
        try:
            c = input(PAD + paint("user name (blank = back) > ", "cyan",
                                  "bold")).strip()
        except (EOFError, KeyboardInterrupt):
            return prog
        if not c:
            return prog
        if c.lower().startswith("user "):           # forgive "user alice"
            c = c[5:].strip()
        prog = cmd_user(c, puzzles, by_id, prog)


def _menu_shortcuts():
    print("")
    print(header("shortcuts", "cyan"))
    print("")
    _disclaimer()
    print("")
    print(PAD + paint(" 1 ", "byellow", "bold")
          + "  enable for THIS terminal (local, nothing saved)")
    print(PAD + paint(" 2 ", "byellow", "bold")
          + "  install persistently (one line in your startup file)")
    print(PAD + paint(" 3 ", "byellow", "bold")
          + "  uninstall (remove the persistent line)")
    print(PAD + paint(" 4 ", "byellow", "bold") + "  back")
    try:
        c = input(PAD + paint("> ", "cyan", "bold")).strip().lower()
    except (EOFError, KeyboardInterrupt):
        return
    if c in ("1", "local"):
        print(PAD + paint("Run this yourself (a program can't source into your "
                          "shell):", "gray"))
        print(PAD + paint(_local_source_cmd(), "yellow", "bold"))
    elif c in ("2", "persist", "install"):
        cmd_setup_persist()
    elif c in ("3", "uninstall", "remove"):
        cmd_uninstall()
