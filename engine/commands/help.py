"""The `help` verb: the one-screen command reference."""

import os

from ..render import paint, wordmark, PAD


def cmd_help():
    print(wordmark("cyan"))
    print("")
    rows = [
        ("begin", "open the main menu (start here)"),
        ("menu", "return to the main menu from anywhere"),
        ("setup", "set up the short commands (offers local or persistent)"),
        ("uninstall", "remove the persistent shortcuts"),
        ("(none)", "show progress and the current puzzle"),
        ("check", "validate your work.py"),
        ("hint", "reveal the next hint"),
        ("solution", "show the reference solution"),
        ("map", "show the chapter/puzzle tree"),
        ("next", "move on to the next puzzle"),
        ("goto", "pick a puzzle from a list (bare goto opens the picker)"),
        ("goto <id>", "jump straight there: goto 2.4, or goto 2 for chapter 2"),
        ("skip", "move on without solving the current puzzle"),
        ("retry", "blank the workspace to practice again (stays solved)"),
        ("revert", "fully reset this puzzle: blank code + clear its progress"),
        ("mode <m>", "set difficulty: easy | normal | hard"),
        ("theme <name>", "switch colour theme (neon, amber, forest, mono)"),
        ("user <name>", "switch or create a profile"),
        ("reset", "wipe progress, saved answers, and workspaces"),
        ("export", "save this profile's progress to a portable file"),
        ("import <file>", "load a profile from an exported file"),
    ]
    pre = "" if os.environ.get("PYQUEST_SHELL") else "python3 play.py "
    for name, desc in rows:
        print("%s%s  %s"
              % (PAD, paint((pre + name).ljust(24), "green", "bold"), desc))
