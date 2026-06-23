"""The interactive launcher menu -- one of two opt-in interactive surfaces (the
other is the play cockpit, cards.nav_select / app._play; see docs/ARCHITECTURE.md
sec 3, invariant 8). The puzzle-solving loop stays single-shot commands; this
sits on top of the verbs, composing cards + profiles + shortcuts.
"""

import sys

from ..config import load_settings, save_settings, MODES, WIDTH, term_size
from ..state import (current_puzzle, activate, load_answers, current_user,
                     list_users)
from ..render import paint, wordmark, header, pane_open, cli, PAD, OK, CUR
from .. import keys
from .. import i18n
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
                   "shortcuts", "short", "language", "lang")


def _leaving(answer):
    return not answer or answer.strip().lower() in _BACK


def _nav_label(label):
    """Localized display text for a hub nav item, keyed off its English label so
    _NAV (dispatch numbers) and the shown wording stay one source of truth."""
    return i18n.t("menu.lbl." + label.replace(" ", "_"), label)
from .shortcuts import (_is_persistent, _disclaimer, _local_source_cmd,
                        cmd_setup_persist, cmd_uninstall)


def cmd_menu(puzzles, by_id, prog):
    """Open the main hub -- the launcher's interactive surface. Reachable from
    anywhere (`menu`, or `back`), and where a cold launch and a bare invocation
    both land."""
    if not sys.stdin.isatty():
        print(wordmark("cyan"))
        _menu_options(puzzles, by_id, prog)
        print(PAD + paint(i18n.t("menu.tty_only",
                          "(run this in a terminal to choose)"), "gray"))
        return
    while True:
        # Redraw the wordmark each time we land on the hub -- on first entry and
        # on every return from a submenu (settings, level) or an inline verb --
        # so "back to the main menu" always shows the same banner, never a bare
        # option list under whatever the submenu left on screen.
        print(wordmark("cyan"))
        raw = _menu_input(puzzles, by_id, prog)
        if raw is None:                          # Ctrl-C / EOF -> leave the hub
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
                    print(PAD + paint(i18n.t("ui.no_puzzle",
                                      "no puzzle '%s'.") % arg, "yellow"))
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
            print(PAD + paint(i18n.t("menu.see_you",
                              "see you in the terminal -- solve with  ")
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
                    print(PAD + paint(i18n.t("menu.verb_needs_puzzle",
                                      "'%s' runs in your terminal, once a "
                                      "puzzle is open.") % verb, "yellow"))
                    print(PAD + i18n.t("menu.verb_needs_puzzle_2",
                          "Pick %s to start, then save work.py and run  %s")
                          % (paint("1", "byellow", "bold"),
                             paint(cli(verb), "cyan", "bold")))
                else:
                    print(PAD + paint(i18n.t("menu.verb_terminal",
                                      "'%s' is a terminal command, not a menu "
                                      "option.") % verb, "yellow"))
                    print(PAD + i18n.t("menu.verb_terminal_2",
                          "Leave the menu (%s) and run  %s")
                          % (paint("0", "byellow", "bold"),
                             paint(cli(verb), "cyan", "bold")))
            else:
                print(PAD + paint(i18n.t("menu.type_number",
                                  "type a number 0-6, or a command."), "yellow"))
        print("")


# The hub items the arrow-navigator steps through, top to bottom: (number, short
# label). One source of truth -- _NAV (the dispatch numbers) and _NAV_LABELS (the
# compact selector's prompt text) are derived, so they can't drift out of sync.
# The labels stay English here (the canonical keys); _nav_label localizes them
# for display, so the dispatch numbers and the shown wording never diverge.
_NAV_ITEMS = (("1", "start"), ("2", "select level"), ("3", "textbook"),
              ("4", "stats"), ("5", "map"), ("6", "settings"), ("0", "quit"))
_NAV = tuple(n for n, _ in _NAV_ITEMS)
_NAV_LABELS = tuple(label for _, label in _NAV_ITEMS)


def _menu_lines(puzzles, by_id, prog, sel=None):
    """The hub body as a flat list of single visual lines, highlighting the item
    whose number == `sel` (None highlights nothing). Returns rather than prints,
    so the arrow-navigator can repaint it in place; `_menu_options` prints it."""
    done, total = len(prog["completed"]), len(puzzles)
    cur = current_puzzle(prog, by_id, puzzles)
    hard = prog["mode"] == "hard"
    L = [""]
    # at-a-glance progress belongs on the hub itself (same opener every pane
    # uses); pane_open is multi-line, so split it into single rows for repaint
    L += pane_open(i18n.t("menu.main_title", "main menu"), prog["mode"],
                   done, total).split("\n")
    L.append("")

    def group(title):
        L.append(PAD + paint(title, "magenta", "bold"))

    def item(n, lbl, note=""):
        on = n == sel
        mark = paint(CUR, "bcyan", "bold") if on else " "
        chip = paint(" %s " % n, "bgreen" if on else "byellow", "bold")
        L.append(PAD + mark + " " + chip + " "
                 + paint(lbl.ljust(13), "bgreen" if on else "white", "bold")
                 + paint(note, "gray"))

    title = cur["meta"].get("title", "") if cur else ""
    where = ("%s · %s" % (cur["id"], title[:40]) if cur else "-")
    group(i18n.t("menu.play", "play"))
    item("1", _nav_label("start"), where)
    item("2", _nav_label("select level"),
         i18n.t("menu.note.select", "jump to any puzzle"))
    L.append("")
    group(i18n.t("menu.learn", "learn"))
    item("3", _nav_label("textbook"),
         i18n.t("menu.note.textbook_sealed", "sealed in hard mode") if hard
         else i18n.t("menu.note.textbook", "syntax & tips so far"))
    item("4", _nav_label("stats"),
         i18n.t("menu.note.stats", "attempts · hints · pace"))
    item("5", _nav_label("map"),
         i18n.t("menu.note.map", "the chapter / puzzle tree"))
    L.append("")
    group(i18n.t("menu.setup", "set up"))
    item("6", _nav_label("settings"),
         i18n.t("menu.note.settings", "theme · mode · profiles · shortcuts"))
    L.append("")
    item("0", _nav_label("quit"))
    L.append("")
    L.append(PAD + paint(i18n.t("menu.footer_full",
                         "arrows move · Enter chooses · type a verb · help"),
                         "gray"))
    return L


def _menu_options(puzzles, by_id, prog):
    print("\n".join(_menu_lines(puzzles, by_id, prog)))


def _fits(n_lines):
    """Is the terminal wide and tall enough to repaint a block of n_lines in
    place? If not, the navigator would wrap/scroll, so the hub uses the compact
    selector (or, with no keys, the typed prompt). The block only needs to FIT
    (lines >= n_lines) -- demanding spare rows wrongly rejected short windows."""
    cols, rows = term_size()
    return cols >= WIDTH and rows >= n_lines


def _hub_navigate(render):
    """Drive a hub selection through keys.navigate (Esc ignored -- 0/quit is the
    explicit exit), translating Ctrl-C/EOF to None. Returns int | str | None."""
    try:
        return keys.navigate(render, len(_NAV), index=0,
                             allow_typing=True, esc_cancels=False)
    except KeyboardInterrupt:
        return None


def _menu_input(puzzles, by_id, prog):
    """Read one hub command. Arrow-navigate the items wherever the terminal
    supports raw input -- in-list highlight when the whole menu fits, else a
    compact one-line selector that fits ANY size (a short Codespaces/VS Code
    panel can't show the full block, but the menu is still navigable) -- and the
    typed prompt only when keys aren't available at all. Returns the command
    string (a chosen number or a typed line), or None to leave the hub."""
    body = _menu_lines(puzzles, by_id, prog)
    if keys.supported() and _fits(len(body) + 1):
        def render(index, buf):                 # full in-list highlight
            sel = None if buf else _NAV[index]
            return (_menu_lines(puzzles, by_id, prog, sel=sel)
                    + [PAD + paint("> ", "cyan", "bold") + buf])
        res = _hub_navigate(render)
    elif keys.supported():
        print("\n".join(body))                  # menu scrolls; selector is 2 lines

        def render(index, buf):                 # size-independent compact selector
            if buf:
                line = PAD + paint("> ", "cyan", "bold") + buf
            else:
                line = (PAD + paint("> ", "cyan", "bold")
                        + paint("%s %s" % (CUR, _nav_label(_NAV_LABELS[index])),
                                "byellow", "bold"))
            return [line, PAD + paint(i18n.t("menu.footer_compact",
                                      "arrows select · Enter runs it · "
                                      "type a verb"), "gray")]
        res = _hub_navigate(render)
    else:
        print("\n".join(body))
        try:
            return input(PAD + paint("> ", "cyan", "bold")).strip()
        except (EOFError, KeyboardInterrupt):
            return None
    if res is None:                             # Ctrl-C / EOF -> leave the hub
        return None
    return (res if isinstance(res, str) else _NAV[res]).strip()


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
    elif head in ("5", "language", "lang"):
        _apply_language(arg) if arg else _menu_language()
    else:
        return False, prog
    return True, prog


def _menu_setup(puzzles, by_id, prog):
    """The folded set-up pane: theme, mode, profiles, shortcuts behind one menu
    entry. Stays open until 0/back. Returns prog (the profile pane can swap it)."""
    labels = ("theme", "mode", "profiles", "shortcuts", "language")
    while True:
        print("")
        print(header(i18n.t("settings.title", "settings"), "cyan"))
        print("")
        notes = (load_settings().get("theme", "neon"), prog["mode"],
                 current_user(),
                 i18n.t("settings.persistent", "persistent: %s")
                 % (i18n.t("ui.on", "on") if _is_persistent()
                    else i18n.t("ui.off", "off")),
                 i18n.current())
        loc = [i18n.t("settings.lbl." + l, l) for l in labels]
        if keys.supported():
            opts = ["%s   %s" % (l.ljust(11), n) for l, n in zip(loc, notes)]
            res = keys.pick("settings", opts, allow_typing=True)
            if res is None:
                return prog
            if isinstance(res, int):
                _, prog = _settings_action(str(res + 1), "", puzzles, by_id, prog)
            elif _leaving(res):
                return prog
            else:
                parts = res.split(None, 1)
                arg = parts[1] if len(parts) > 1 else ""
                handled, prog = _settings_action(parts[0].lower(), arg,
                                                 puzzles, by_id, prog)
                if not handled:
                    print(PAD + paint(i18n.t("settings.type_hint",
                                      "type theme / mode / profiles / "
                                      "shortcuts, or Esc."), "yellow"))
            continue

        def item(n, lbl, note=""):
            print(PAD + paint(" %s " % n, "byellow", "bold") + "  "
                  + paint(lbl.ljust(11), "white", "bold") + paint(note, "gray"))

        for i, lbl in enumerate(loc):
            item(str(i + 1), lbl, notes[i])
        print("")
        item("0", i18n.t("ui.back", "back"))
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
            print(PAD + paint(i18n.t("settings.type_number",
                              "type 1-4, or 0 to go back."), "yellow"))


def _menu_mode(prog):
    # Pick a difficulty: arrow-keys + Enter where the terminal supports raw
    # input (keys.pick), else the typed prompt. Blank line / 0 / ESC cancels.
    # Mirrors the theme/users panes.
    while True:
        print("")
        print(header(i18n.t("mode.picker_title", "difficulty"), "cyan"))
        print("")
        if keys.supported():
            cur = prog.get("mode")
            start = MODES.index(cur) if cur in MODES else 0
            i = keys.pick("difficulty", list(MODES), index=start)
            if i is not None:                       # ESC / q / Ctrl-C -> back
                cmd_mode(prog, MODES[i])            # sets + persists
            return
        for m in MODES:
            on = m == prog.get("mode")
            print(PAD + " %s  %s"
                  % (paint(OK if on else "·", "green" if on else "gray"),
                     paint(m.ljust(7), "byellow" if on else "white", "bold")))
        print("")
        try:
            c = input(PAD + paint(i18n.t("mode.prompt",
                                  "easy / normal / hard  (0 = back) > "),
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
    # same lock rules as goto either way -- the menu must not be a side door
    if keys.supported():
        labels = ["%s · %s" % (p["id"], p["meta"].get("title", ""))
                  for p in puzzles]
        cur = current_puzzle(prog, by_id, puzzles)
        start = next((i for i, p in enumerate(puzzles)
                      if cur and p["id"] == cur["id"]), 0)
        print("")
        print(header(i18n.t("menu.level_title", "select level"), "cyan"))
        res = keys.pick("level", labels, index=start, allow_typing=True,
                        max_rows=12)
        if res is None:
            return
        if isinstance(res, int):
            _jump(puzzles[res], puzzles, by_id, prog)
            return
        target = _resolve_goto(res, puzzles, by_id, prog)
        if target is None:
            print(PAD + paint(i18n.t("ui.no_puzzle", "no puzzle '%s'.") % res,
                              "yellow"))
        else:
            _jump(target, puzzles, by_id, prog)
        return
    _goto_list(puzzles, by_id, prog, footer=False)
    try:
        pid = input(PAD + paint(i18n.t("menu.level_prompt", "id  (0 = back) > "),
                                "cyan", "bold")).strip()
    except (EOFError, KeyboardInterrupt):
        return
    if _leaving(pid):
        return
    target = _resolve_goto(pid, puzzles, by_id, prog)
    if target is None:
        print(PAD + paint(i18n.t("ui.no_puzzle", "no puzzle '%s'.") % pid,
                          "yellow"))
        return
    _jump(target, puzzles, by_id, prog)


def _menu_theme():
    if keys.supported():
        from ..theme import THEMES, load_presets
        names = list(THEMES) + [p for p in load_presets() if p not in THEMES]
        cur = load_settings().get("theme", "neon")
        print("")
        print(header(i18n.t("theme.picker_title", "theme"), "cyan"))
        res = keys.pick("theme", names,
                        index=names.index(cur) if cur in names else 0,
                        allow_typing=True)
        if res is None:
            return
        cmd_theme(names[res] if isinstance(res, int) else res.lower())
        return
    # Stay in the theme picker until 0/back (the rule) or a blank line.
    while True:
        cmd_theme("")                               # show the picker
        try:
            c = input(PAD + paint(i18n.t("theme.prompt",
                                  "theme name  (0 = back) > "), "cyan",
                                  "bold")).strip().lower()
        except (EOFError, KeyboardInterrupt):
            return
        if _leaving(c):
            return
        if c.startswith("theme "):                  # forgive "theme ocean"
            c = c[6:].strip()
        cmd_theme(c)                                # applies + persists live


def _apply_language(code):
    """Switch UI language to `code` and persist it. On a bad pack, print what's
    missing and stay on English -- i18n.set_language has already fallen back."""
    code = (code or "").strip()
    ok, msg = i18n.set_language(code or "en")
    if not ok:
        print(PAD + paint(msg, "yellow"))           # names the missing file/field
        return
    settings = load_settings()
    settings["lang"] = i18n.current()
    save_settings(settings)
    print(PAD + paint(i18n.t("lang.set", "language set to %s.")
                      % i18n.current(), "green", "bold"))


def _menu_language():
    """Pick the UI language. The list is English plus every pack under lang/ that
    loads; a contributor drops a folder in (see lang/README.md) and it appears."""
    langs = i18n.available()                         # [(code, name), ...], en first
    cur = i18n.current()
    start = next((i for i, (c, _) in enumerate(langs) if c == cur), 0)
    if keys.supported():
        print("")
        print(header(i18n.t("lang.picker_title", "language"), "cyan"))
        i = keys.pick("language", ["%s  (%s)" % (n, c) for c, n in langs],
                      index=start)
        if i is not None:
            _apply_language(langs[i][0])
        return
    print("")
    print(header(i18n.t("lang.picker_title", "language"), "cyan"))
    for c, n in langs:
        on = c == cur
        print(PAD + " %s  %s  %s"
              % (paint(OK if on else "·", "green" if on else "gray"),
                 paint(n.ljust(12), "byellow" if on else "white", "bold"),
                 paint("(%s)" % c, "gray")))
    print("")
    try:
        c = input(PAD + paint(i18n.t("lang.prompt",
                              "language code  (0 = back) > "), "cyan",
                              "bold")).strip()
    except (EOFError, KeyboardInterrupt):
        return
    if not _leaving(c):
        _apply_language(c)


def _menu_users(puzzles, by_id, prog):
    # Stay in the profiles pane until 0/back (the rule), Esc, or a blank line.
    while True:
        if keys.supported():
            names = list_users()
            cur = current_user()
            print("")
            print(header(i18n.t("profiles.title", "profiles"), "cyan"))
            print(PAD + paint(i18n.t("profiles.arrow_hint",
                              "arrow to a name to switch · or type "
                              "'rename a b' / 'delete a'"), "gray"))
            res = keys.pick("profiles", names,
                            index=names.index(cur) if cur in names else 0,
                            allow_typing=True)
            if res is None:
                return prog
            choice = names[res] if isinstance(res, int) else res
            if choice.lower().startswith("user "):
                choice = choice[5:].strip()
            # cmd_user parses bare names plus delete/rename subcommands.
            prog = cmd_user(choice, puzzles, by_id, prog)
            continue
        cmd_user("", puzzles, by_id, prog)          # list users + management help
        try:
            c = input(PAD + paint(i18n.t("profiles.prompt",
                                  "name to switch · 'rename a b' · "
                                  "'delete a'  (0 = back) > "), "cyan",
                                  "bold")).strip()
        except (EOFError, KeyboardInterrupt):
            return prog
        if _leaving(c):
            return prog
        if c.lower().startswith("user "):           # forgive "user alice"
            c = c[5:].strip()
        prog = cmd_user(c, puzzles, by_id, prog)


def _menu_shortcuts():
    print("")
    print(header(i18n.t("shortcuts.title", "shortcuts"), "cyan"))
    print("")
    _disclaimer()
    print("")
    print(PAD + paint(" 1 ", "byellow", "bold")
          + "  " + i18n.t("shortcuts.opt_local",
                          "enable for THIS terminal (local, nothing saved)"))
    print(PAD + paint(" 2 ", "byellow", "bold")
          + "  " + i18n.t("shortcuts.opt_persist",
                          "install persistently (one line in your startup file)"))
    print(PAD + paint(" 3 ", "byellow", "bold")
          + "  " + i18n.t("shortcuts.opt_uninstall",
                          "uninstall (remove the persistent line)"))
    print(PAD + paint(" 0 ", "byellow", "bold") + "  "
          + i18n.t("ui.back", "back"))
    try:
        c = input(PAD + paint("> ", "cyan", "bold")).strip().lower()
    except (EOFError, KeyboardInterrupt):
        return
    if _leaving(c):
        return
    if c in ("1", "local"):
        print(PAD + paint(i18n.t("shortcuts.run_yourself",
                          "Run this yourself (a program can't source into your "
                          "shell):"), "gray"))
        print(PAD + paint(_local_source_cmd(), "yellow", "bold"))
    elif c in ("2", "persist", "install"):
        cmd_setup_persist()
    elif c in ("3", "uninstall", "remove"):
        cmd_uninstall()
