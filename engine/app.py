"""Argv dispatch and entry point. Wires the command verbs together."""

import sys

from .config import CHAPTERS_DIR, rel
from .content import discover
from .state import (load_progress, current_puzzle, ensure_workspace,
                    load_answers, migrate_legacy)
from .render import paint, cli, STAR, NO, PAD
from .checker import cmd_check
from .commands import (cmd_status, cmd_map, cmd_stats, cmd_hint, cmd_solution,
                       cmd_textbook, cmd_next,
                       cmd_goto, cmd_skip, cmd_retry, cmd_restart, cmd_mode,
                       cmd_theme, cmd_user, cmd_wipe, cmd_export, cmd_import,
                       cmd_setup, cmd_setup_persist, cmd_uninstall,
                       cmd_menu, cmd_help)
from .commands.registry import canonical, NEEDS_PUZZLE, suggest


def main():
    puzzles = discover()
    if not puzzles:
        print("No puzzles found under %s" % rel(CHAPTERS_DIR))
        return
    by_id = {p["id"]: p for p in puzzles}
    migrate_legacy()                 # seed users/ and move any legacy root files
    prog, fresh = load_progress(puzzles)
    prog.setdefault("mode", "normal")
    prog.setdefault("completed", [])
    prog.setdefault("stats", {})
    prog.setdefault("highest", 0)
    # existing learners (already have progress) count as active
    prog.setdefault("active", len(prog.get("completed", [])) > 0)

    args = sys.argv[1:]
    # Bare invocation (`start` / `python3 start.py` inside a session) always
    # opens the menu -- the same place a cold launch lands. `status` and every
    # other view stay one explicit word away (`start status`, `status`).
    raw = args[0].lower() if args else "menu"
    cmd = canonical(raw)                 # fold aliases (load->goto, replay->retry)
    arg = args[1] if len(args) > 1 else None
    arg2 = args[2] if len(args) > 2 else None
    arg3 = args[3] if len(args) > 3 else None

    # make sure work.py exists (welcome placeholder until a puzzle is loaded)
    ensure_workspace(current_puzzle(prog, by_id, puzzles), load_answers(),
                     prog.get("active"))

    # First run: greet the learner wherever a bare launch lands them. That is
    # the menu now, but an explicit `status` should still welcome too.
    if fresh and cmd in ("status", "menu"):
        print(paint("  %s  Welcome to PyQuest!" % STAR, "cyan", "bold"))
        if cmd == "status":
            print("  Open the menu to set up and pick a level:  %s\n"
                  % cli("menu"))
        else:
            print("  Set up and pick a level from the menu below.\n")

    # Context gate: the puzzle-logic verbs only mean something with a puzzle
    # loaded. Without one the learner is between the two command sets, so route
    # them to the menu (the home base) rather than dead-ending on a message.
    if cmd in NEEDS_PUZZLE and not prog.get("active"):
        print(paint("  %s  No puzzle loaded yet -- here's the menu." % NO,
                    "yellow"))
        cmd_menu(puzzles, by_id, prog)
        return

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
        cmd_menu(puzzles, by_id, prog)
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
            print(paint("  Unknown command '%s'. Did you mean  %s ?"
                        % (raw, cli(near)), "yellow"))
            print(PAD + paint("run  %s  for the full list." % cli("help"),
                              "gray"))
        else:
            print(paint("  Unknown command '%s'." % raw, "yellow"))
            cmd_help(prog)
