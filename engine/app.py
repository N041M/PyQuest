"""Argv dispatch and entry point. Wires the command verbs together."""

import sys

from .config import CHAPTERS_DIR, rel
from .content import discover
from .state import (load_progress, current_puzzle, ensure_workspace,
                    load_answers, migrate_legacy)
from .render import paint, cli, STAR, NO, PAD
from .checker import cmd_check
from .commands import (cmd_status, cmd_map, cmd_hint, cmd_solution, cmd_next,
                       cmd_goto, cmd_skip, cmd_retry, cmd_revert, cmd_mode,
                       cmd_theme, cmd_user, cmd_reset, cmd_export, cmd_import,
                       cmd_setup, cmd_setup_persist, cmd_uninstall, cmd_begin,
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
    raw = args[0].lower() if args else "status"
    cmd = canonical(raw)                 # fold aliases (load->goto, replay->retry)
    arg = args[1] if len(args) > 1 else None
    arg2 = args[2] if len(args) > 2 else None
    arg3 = args[3] if len(args) > 3 else None

    # make sure work.py exists (welcome placeholder until a puzzle is loaded)
    ensure_workspace(current_puzzle(prog, by_id, puzzles), load_answers(),
                     prog.get("active"))

    if fresh and cmd == "status":
        print(paint("  %s  Welcome to PyQuest!" % STAR, "cyan", "bold"))
        print("  Open the menu to set up and pick a level:  %s\n"
              % cli("begin"))

    # Context gate: verbs that act on the current puzzle need one loaded first.
    # Redirect to the menu instead of running a verb with nothing to act on.
    if cmd in NEEDS_PUZZLE and not prog.get("active"):
        print(paint("  %s  '%s' needs a puzzle loaded first." % (NO, cmd),
                    "yellow"))
        print("  Open the menu with %s, or jump straight in with %s."
              % (cli("begin"), cli("goto 1.1")))
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
    elif cmd == "next":
        cmd_next(puzzles, by_id, prog)
    elif cmd == "goto":
        cmd_goto(puzzles, by_id, prog, arg)
    elif cmd == "skip":
        cmd_skip(puzzles, by_id, prog)
    elif cmd == "retry":
        cmd_retry(puzzles, by_id, prog)
    elif cmd == "revert":
        cmd_revert(puzzles, by_id, prog)
    elif cmd == "mode":
        cmd_mode(prog, arg)
    elif cmd == "theme":
        cmd_theme(arg)
    elif cmd == "user":
        cmd_user(arg, puzzles, by_id, prog)
    elif cmd == "reset":
        cmd_reset(puzzles, prog, arg)
    elif cmd == "export":
        cmd_export(puzzles, by_id, prog, arg)
    elif cmd == "import":
        cmd_import(puzzles, by_id, prog, arg, arg2, arg3)
    elif cmd == "begin":
        cmd_begin(puzzles, by_id, prog)
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
        cmd_help()
    else:
        near = suggest(raw)
        if near:
            print(paint("  Unknown command '%s'. Did you mean  %s ?"
                        % (raw, cli(near)), "yellow"))
            print(PAD + paint("run  %s  for the full list." % cli("help"),
                              "gray"))
        else:
            print(paint("  Unknown command '%s'." % raw, "yellow"))
            cmd_help()
