"""The interactive launcher menu -- the one allowed interactive surface (see
docs/ARCHITECTURE.md sec 3, invariant 8a). The puzzle-solving loop stays single-shot
commands; this sits on top of the verbs, composing cards + profiles + shortcuts.
"""

import sys

from ..config import load_settings, MODES
from ..state import current_puzzle, activate, load_answers, current_user
from ..render import paint, wordmark, header, pane_open, cli, PAD, OK
from .cards import print_current_card, _goto_list, _resolve_goto, _jump
from .profiles import cmd_theme, cmd_user, cmd_mode
from .views import cmd_status, cmd_map, cmd_search, cmd_stats, cmd_textbook
from .navigate import cmd_resume
from .help import cmd_help
from .registry import canonical, CANONICAL, NEEDS_PUZZLE

# Read-only inspection verbs with no number of their own: typed at the hub, they
# only print, so it runs them inline rather than kicking the learner to a
# terminal. (map/stats/textbook have menu numbers; they're dispatched there.)
_INLINE = {"help": lambda pz, by, pr: cmd_help(pr),
           "status": lambda pz, by, pr: cmd_status(pz, by, pr)}

# The rule, applied in every pane: 0 (and its words) always backs out. A blank
# line cancels too. `_leaving` keeps the check identical everywhere.
_BACK = ("0", "back", "quit", "exit")

# Settings verbs the hub accepts typed by name (numbers 1-6 are claimed by the
# hub's own menu, so only the settings PANE passes the 1-4 aliases that
# _settings_action also understands).
_SETTINGS_VERBS = ("theme", "mode", "profiles", "profile", "users", "user",
                   "shortcuts", "short")


def _leaving(answer):
    return not answer or answer.strip().lower() in _BACK
from .shortcuts import (_is_persistent, _disclaimer, _local_source_cmd,
                        cmd_setup_persist, cmd_uninstall)


def cmd_menu(puzzles, by_id, prog):
    """Open the main hub -- the one interactive surface. Reachable from anywhere
    (`menu`, or `back`), and where a cold launch and a bare invocation both land."""
    if not sys.stdin.isatty():
        print(wordmark("cyan"))
        _menu_options(puzzles, by_id, prog)
        print(PAD + paint("(run this in a terminal to choose)", "gray"))
        return
    print(wordmark("cyan"))
    while True:
        _menu_options(puzzles, by_id, prog)
        try:
            raw = input(PAD + paint("> ", "cyan", "bold")).strip()
        except (EOFError, KeyboardInterrupt):
            print("")
            return
        # Split into a verb + the rest, so "goto 2.4", "theme ocean" and
        # "user alice" work as one line. The head matches case-insensitively;
        # the argument keeps its case (usernames are case-sensitive).
        parts = raw.split(None, 1)
        head = parts[0].lower() if parts else ""
        arg = parts[1] if len(parts) > 1 else ""
        # -- play --
        if head in ("1", "start", "continue", "play", ""):
            cur = current_puzzle(prog, by_id, puzzles)
            activate(prog, cur, load_answers())     # load the puzzle into work.py
            print("")
            print_current_card(prog, cur, arriving=True, puzzles=puzzles)
            return
        elif head in ("2", "level", "select", "goto", "load"):
            if arg:                                 # "goto 2.4" -- jump straight
                target = _resolve_goto(arg, puzzles, by_id, prog)
                if target is None:
                    print(PAD + paint("no puzzle '%s'." % arg, "yellow"))
                else:
                    _jump(target, puzzles, by_id, prog)
            else:
                _menu_level(puzzles, by_id, prog)
        elif head in ("resume",):                    # jump to first unsolved, then go
            cmd_resume(puzzles, by_id, prog)
            return
        elif head in ("search", "find"):             # discovery, runs in place
            print("")
            cmd_search(puzzles, by_id, prog, arg)
        # -- learn (read-only verbs, run in place) --
        elif head in ("3", "textbook", "ref"):       # "textbook all" reads here too
            print("")
            cmd_textbook(puzzles, by_id, prog, arg)
        elif head in ("4", "stats", "score"):
            print("")
            cmd_stats(puzzles, by_id, prog)
        elif head in ("5", "map"):
            print("")
            cmd_map(puzzles, by_id, prog)
        # -- set up (folded into one submenu) --
        elif head in ("6", "set", "setup", "settings"):
            prog = _menu_setup(puzzles, by_id, prog)
        # The settings verbs still work typed straight at the hub, with an arg,
        # for anyone who knows them -- they're just no longer numbered up front.
        elif head in _SETTINGS_VERBS:
            _, prog = _settings_action(head, arg, puzzles, by_id, prog)
        # -- leave (the rule: 0 always backs out / quits) --
        elif head in _BACK or head == "q":
            print(PAD + paint("see you in the terminal -- solve with  "
                              + cli("check"), "gray"))
            return
        elif canonical(head) in _INLINE:
            print("")                               # run inspection verbs in place
            _INLINE[canonical(head)](puzzles, by_id, prog)
        else:
            # A learner often types a real verb (check, hint, next...) at this
            # prompt. The menu picks options 0-6, so point them at where that
            # verb actually runs instead of a dead-end "type a number".
            verb = canonical(head)
            if verb in CANONICAL and verb != "menu":
                if verb in NEEDS_PUZZLE:
                    print(PAD + paint("'%s' runs in your terminal, once a "
                                      "puzzle is open." % verb, "yellow"))
                    print(PAD + "Pick %s to start, then save work.py and run  %s"
                          % (paint("1", "byellow", "bold"),
                             paint(cli(verb), "cyan", "bold")))
                else:
                    print(PAD + paint("'%s' is a terminal command, not a menu "
                                      "option." % verb, "yellow"))
                    print(PAD + "Leave the menu (%s) and run  %s"
                          % (paint("0", "byellow", "bold"),
                             paint(cli(verb), "cyan", "bold")))
            else:
                print(PAD + paint("type a number 0-6, or a command.", "yellow"))
        print("")


def _menu_options(puzzles, by_id, prog):
    done, total = len(prog["completed"]), len(puzzles)
    cur = current_puzzle(prog, by_id, puzzles)
    hard = prog["mode"] == "hard"
    print("")
    # at-a-glance progress belongs on the hub itself (same opener every pane
    # uses), not in a tab of its own
    print(pane_open("main menu", prog["mode"], done, total))
    print("")

    def group(title):
        print(PAD + paint(title, "magenta", "bold"))

    def item(n, lbl, note=""):
        print(PAD + paint(" %s " % n, "byellow", "bold") + "  "
              + paint(lbl.ljust(13), "white", "bold") + paint(note, "gray"))

    where = ("%s · %s" % (cur["id"], cur["meta"].get("title", ""))
             if cur else "-")
    group("play")
    item("1", "start", where)
    item("2", "select level", "jump to any puzzle")
    print("")
    group("learn")
    item("3", "textbook", "sealed in hard mode" if hard
         else "syntax & tips so far")
    item("4", "stats", "attempts · hints · pace")
    item("5", "map", "the chapter / puzzle tree")
    print("")
    group("set up")
    item("6", "settings", "theme · mode · profiles · shortcuts")
    print("")
    item("0", "quit")
    print("")
    print(PAD + paint("pick a number, type a verb, or  help", "gray"))


def _settings_action(head, arg, puzzles, by_id, prog):
    """Run one settings verb -- theme / mode / profiles / shortcuts -- with an
    optional arg, falling back to that verb's picker when no arg is given.

    The single dispatch shared by the hub (where the verbs are typed by name)
    and the settings pane (where they're picked by number), so the mapping lives
    in one place instead of two that can drift. Returns (handled, prog); handled
    is False when `head` names no settings verb."""
    if head in ("1", "theme"):
        cmd_theme(arg.lower()) if arg else _menu_theme()
    elif head in ("2", "mode"):
        cmd_mode(prog, arg) if arg else _menu_mode(prog)
    elif head in ("3", "profiles", "profile", "users", "user"):
        prog = (cmd_user(arg, puzzles, by_id, prog) if arg
                else _menu_users(puzzles, by_id, prog))
    elif head in ("4", "shortcuts", "short"):
        _menu_shortcuts()
    else:
        return False, prog
    return True, prog


def _menu_setup(puzzles, by_id, prog):
    """The folded set-up pane: theme, mode, profiles, shortcuts behind one menu
    entry. Stays open until 0/back. Returns prog (the profile pane can swap it)."""
    while True:
        print("")
        print(header("settings", "cyan"))
        print("")

        def item(n, lbl, note=""):
            print(PAD + paint(" %s " % n, "byellow", "bold") + "  "
                  + paint(lbl.ljust(11), "white", "bold") + paint(note, "gray"))

        item("1", "theme", load_settings().get("theme", "neon"))
        item("2", "mode", prog["mode"])
        item("3", "profiles", current_user())
        item("4", "shortcuts", "persistent: %s"
             % ("on" if _is_persistent() else "off"))
        print("")
        item("0", "back")
        print("")
        try:
            raw = input(PAD + paint("> ", "cyan", "bold")).strip()
        except (EOFError, KeyboardInterrupt):
            return prog
        if _leaving(raw):
            return prog
        parts = raw.split(None, 1)
        head = parts[0].lower()
        arg = parts[1] if len(parts) > 1 else ""
        handled, prog = _settings_action(head, arg, puzzles, by_id, prog)
        if not handled:
            print(PAD + paint("type 1-4, or 0 to go back.", "yellow"))


def _menu_mode(prog):
    # Pick a difficulty; blank line cancels. Mirrors the theme/users panes.
    while True:
        print("")
        print(header("difficulty", "cyan"))
        print("")
        for m in MODES:
            on = m == prog.get("mode")
            print(PAD + " %s  %s"
                  % (paint(OK if on else "·", "green" if on else "gray"),
                     paint(m.ljust(7), "byellow" if on else "white", "bold")))
        print("")
        try:
            c = input(PAD + paint("easy / normal / hard  (0 = back) > ",
                                  "cyan", "bold")).strip().lower()
        except (EOFError, KeyboardInterrupt):
            return
        if _leaving(c):
            return
        if c.startswith("mode "):                   # forgive "mode hard"
            c = c[5:].strip()
        cmd_mode(prog, c)                           # sets + persists, or reprints
        if c in MODES:
            return


def _menu_level(puzzles, by_id, prog):
    _goto_list(puzzles, by_id, prog, footer=False)
    try:
        pid = input(PAD + paint("id  (0 = back) > ", "cyan", "bold")).strip()
    except (EOFError, KeyboardInterrupt):
        return
    if _leaving(pid):
        return
    target = _resolve_goto(pid, puzzles, by_id, prog)
    if target is None:
        print(PAD + paint("no puzzle '%s'." % pid, "yellow"))
        return
    # same lock rules as goto -- the menu must not be a side door
    _jump(target, puzzles, by_id, prog)


def _menu_theme():
    # Stay in the theme picker until 0/back (the rule) or a blank line.
    while True:
        cmd_theme("")                               # show the picker
        try:
            c = input(PAD + paint("theme name  (0 = back) > ", "cyan",
                                  "bold")).strip().lower()
        except (EOFError, KeyboardInterrupt):
            return
        if _leaving(c):
            return
        if c.startswith("theme "):                  # forgive "theme ocean"
            c = c[6:].strip()
        cmd_theme(c)                                # applies + persists live


def _menu_users(puzzles, by_id, prog):
    # Stay in the profiles pane until 0/back (the rule) or a blank line.
    while True:
        cmd_user("", puzzles, by_id, prog)          # list users + management help
        try:
            c = input(PAD + paint("name to switch · 'rename a b' · "
                                  "'delete a'  (0 = back) > ", "cyan",
                                  "bold")).strip()
        except (EOFError, KeyboardInterrupt):
            return prog
        if _leaving(c):
            return prog
        if c.lower().startswith("user "):           # forgive "user alice"
            c = c[5:].strip()
        # cmd_user parses bare names plus the delete/rename subcommands, so the
        # raw line goes straight through -- the pane is a full profile manager.
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
    print(PAD + paint(" 0 ", "byellow", "bold") + "  back")
    try:
        c = input(PAD + paint("> ", "cyan", "bold")).strip().lower()
    except (EOFError, KeyboardInterrupt):
        return
    if _leaving(c):
        return
    if c in ("1", "local"):
        print(PAD + paint("Run this yourself (a program can't source into your "
                          "shell):", "gray"))
        print(PAD + paint(_local_source_cmd(), "yellow", "bold"))
    elif c in ("2", "persist", "install"):
        cmd_setup_persist()
    elif c in ("3", "uninstall", "remove"):
        cmd_uninstall()
