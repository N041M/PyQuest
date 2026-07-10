"""Argv dispatch and entry point. Wires the command verbs together."""

import sys

from .config import CHAPTERS_DIR, rel, load_settings
from .content import discover
from .state import (load_progress, current_puzzle, ensure_workspace,
                    load_answers, migrate_legacy)
from .render import paint, cli, STAR, NO, PAD
from .i18n import t
from .checker import cmd_check
from .commands import (cmd_status, cmd_map, cmd_search, cmd_stats, cmd_hint,
                       cmd_solution, cmd_textbook, cmd_next, cmd_resume,
                       cmd_note, cmd_goto, cmd_skip, cmd_retry, cmd_restart,
                       cmd_mode,
                       cmd_theme, cmd_user, cmd_wipe, cmd_export, cmd_import,
                       cmd_setup, cmd_setup_persist, cmd_uninstall,
                       cmd_menu, cmd_help)
from .commands import cards
from .commands.registry import canonical, NEEDS_PUZZLE, suggest, _all_names
from . import keys
from . import i18n


def _emit_completions(what, puzzles):
    """Print one candidate per line for shell tab-completion. Sourced by the
    completion functions in shell/, so the candidate lists never drift from the
    real verbs/ids/themes/profiles. A hidden helper -- not a learner command."""
    kind = what[0] if what else "verbs"
    if kind == "ids":
        items = [p["id"] for p in puzzles]
    elif kind == "themes":
        from .theme import THEME_NAMES
        items = list(THEME_NAMES)
    elif kind == "users":
        from .state import list_users
        items = list_users()
    else:
        items = sorted(set(_all_names()))
    print("\n".join(items))


def dispatch(args, puzzles, by_id, prog):
    """Run one verb from `args` (a [verb, *rest] list) and return prog (only
    `user`/`import` can replace it). Shared by the one-shot CLI in main() and the
    interactive play cockpit (_play), so both route through exactly one mapping."""
    raw = args[0].lower() if args else "menu"
    cmd = canonical(raw)                 # fold aliases (load->goto, replay->retry)
    arg = args[1] if len(args) > 1 else None
    arg2 = args[2] if len(args) > 2 else None
    arg3 = args[3] if len(args) > 3 else None
    if cmd == "status":
        cmd_status(puzzles, by_id, prog)
    elif cmd == "check":
        cmd_check(puzzles, by_id, prog)
    elif cmd == "hint":
        cmd_hint(puzzles, by_id, prog)
    elif cmd == "solution":
        cmd_solution(puzzles, by_id, prog)
    elif cmd == "map":
        cmd_map(puzzles, by_id, prog)
    elif cmd == "search":
        cmd_search(puzzles, by_id, prog, arg)
    elif cmd == "resume":
        cmd_resume(puzzles, by_id, prog)
    elif cmd == "stats":
        cmd_stats(puzzles, by_id, prog)
    elif cmd == "textbook":
        cmd_textbook(puzzles, by_id, prog, arg)
    elif cmd == "next":
        cmd_next(puzzles, by_id, prog)
    elif cmd == "goto":
        cmd_goto(puzzles, by_id, prog, arg)
    elif cmd == "skip":
        cmd_skip(puzzles, by_id, prog)
    elif cmd == "note":
        # whole tail is the note text, so multi-word notes arrive intact
        cmd_note(puzzles, by_id, prog, " ".join(args[1:]))
    elif cmd == "retry":
        cmd_retry(puzzles, by_id, prog)
    elif cmd == "restart":
        cmd_restart(puzzles, by_id, prog)
    elif cmd == "mode":
        cmd_mode(prog, arg)
    elif cmd == "theme":
        cmd_theme(arg)
    elif cmd == "user":
        # pass the whole tail so `user rename <old> <new>` and `user delete
        # <name>` reach the subcommand parser, not just the first token
        prog = cmd_user(" ".join(args[1:]), puzzles, by_id, prog)
    elif cmd == "wipe":
        cmd_wipe(puzzles, prog, arg)
    elif cmd == "export":
        cmd_export(puzzles, by_id, prog, arg)
    elif cmd == "import":
        cmd_import(puzzles, by_id, prog, arg, arg2, arg3)
    elif cmd == "menu":
        # capture prog: the menu can switch profile (a new prog), and _play must
        # run against that, not the pre-menu one -- else the card and the checker
        # read different progs (card shows the new puzzle, check runs the old).
        prog = cmd_menu(puzzles, by_id, prog)
    elif cmd == "setup":
        if arg == "persist":
            cmd_setup_persist()
        else:
            cmd_setup()
    elif cmd == "uninstall":
        cmd_uninstall()
    elif cmd == "help":
        cmd_help(prog)
    else:
        near = suggest(raw)
        if near:
            print(paint("  " + t("app.unknown_suggest",
                        "Unknown command '%s'. Did you mean  %s ?")
                        % (raw, cli(near)), "yellow"))
            print(PAD + paint(t("app.run_full_list",
                              "run  %s  for the full list.") % cli("help"),
                              "gray"))
        else:
            print(paint("  " + t("app.unknown", "Unknown command '%s'.") % raw,
                        "yellow"))
            cmd_help(prog)
    return prog


def _play(puzzles, by_id, prog):
    """The play cockpit: the card's bottom row made interactive (the one allowed
    on the puzzle screen, alongside the launcher menu). Arrow across the verbs
    and Enter runs one in place; type a verb for anything off the row; Esc drops
    to the shell to edit work.py and run check there, the same as always. Entered
    only when a card was just drawn in an interactive, key-capable terminal."""
    while True:
        cur = current_puzzle(prog, by_id, puzzles)
        if not (prog.get("active") and cur):
            break
        choice = cards.nav_select(prog, cur, puzzles)
        if choice is None:                   # Esc / Ctrl-C -> back to the shell
            break
        print("")
        prog = dispatch(choice.split(), puzzles, by_id, prog)


def main():
    puzzles = discover()
    if not puzzles:
        print(t("app.no_puzzles", "No puzzles found under %s")
              % rel(CHAPTERS_DIR))
        return
    by_id = {p["id"]: p for p in puzzles}
    # Hidden shell-completion hook: emit candidates and exit before any side
    # effects (no workspace seeding, no greeting). Never a learner-facing verb.
    if sys.argv[1:2] == ["__complete"]:
        _emit_completions(sys.argv[2:], puzzles)
        return
    migrate_legacy()                 # seed users/ and move any legacy root files
    prog, fresh = load_progress(puzzles)
    prog.setdefault("mode", "normal")
    prog.setdefault("completed", [])
    prog.setdefault("stats", {})
    prog.setdefault("highest", 0)
    # existing learners (already have progress) count as active
    prog.setdefault("active", len(prog.get("completed", [])) > 0)

    # Activate the saved UI language. English is the default and the fallback:
    # a missing or broken pack reports what's wrong and reverts to English rather
    # than blocking startup.
    lang_ok, lang_msg = i18n.set_language(load_settings().get("lang", "en"))
    if not lang_ok:
        print(paint("  %s  %s" % (NO, lang_msg), "yellow"))

    args = sys.argv[1:]
    # Bare invocation (`start` / `python3 start.py` inside a session) always
    # opens the menu -- the same place a cold launch lands. `status` and every
    # other view stay one explicit word away (`start status`, `status`).
    raw = args[0].lower() if args else "menu"
    cmd = canonical(raw)

    # make sure work.py exists (welcome placeholder until a puzzle is loaded)
    ensure_workspace(current_puzzle(prog, by_id, puzzles), load_answers(),
                     prog.get("active"))

    # The play cockpit (interactive bottom row) needs a key-capable TTY; without
    # one every card keeps its static row and the learner types verbs as before.
    interactive = sys.stdin.isatty() and keys.supported()
    cards.play.active = interactive

    # First run: greet the learner wherever a bare launch lands them. That is
    # the menu now, but an explicit `status` should still welcome too.
    if fresh and cmd in ("status", "menu"):
        print(paint("  %s  " % STAR + t("app.welcome", "Welcome to PyQuest!"),
                    "cyan", "bold"))
        if cmd == "status":
            print("  " + t("app.open_menu_status",
                  "Open the menu to set up and pick a level:  %s\n")
                  % cli("menu"))
        else:
            print("  " + t("app.setup_below",
                  "Set up and pick a level from the menu below.\n"))

    # Context gate: the puzzle-logic verbs only mean something with a puzzle
    # loaded. Without one the learner is between the two command sets, so route
    # them to the menu (the home base) rather than dead-ending on a message.
    if cmd in NEEDS_PUZZLE and not prog.get("active"):
        print(paint("  %s  " % NO + t("app.no_loaded_menu",
                    "No puzzle loaded yet -- here's the menu."), "yellow"))
        cmd_menu(puzzles, by_id, prog)
        return

    cards.play.card_drawn = False
    prog = dispatch(args, puzzles, by_id, prog)
    # If that landed on a puzzle card in an interactive terminal, open the
    # cockpit so the bottom row is selectable; otherwise we just return.
    if interactive and prog.get("active") and cards.play.card_drawn:
        _play(puzzles, by_id, prog)
