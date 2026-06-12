#!/usr/bin/env python3
"""PyQuest -- a terminal-run Python course.

This is a thin launcher. The implementation lives in the `engine/` package,
split by concern (visuals, content, input, checking, state). See ARCHITECTURE.md
for the module map and the rules that keep it modular.

    python3 play.py            show progress + the current puzzle
    python3 play.py begin      open the main menu (also: menu, from anywhere)
    python3 play.py check      validate the current work.py
    python3 play.py hint       reveal the next hint
    python3 play.py solution   show the reference solution
    python3 play.py map        show the chapter/puzzle tree
    python3 play.py goto 3.2   jump to a puzzle (lists choices with no id)
    python3 play.py next       move on to the next puzzle
    python3 play.py retry      clear the current puzzle and solve it again
    python3 play.py mode easy  set difficulty: easy | normal | hard
    python3 play.py reset      wipe progress, answers, and workspaces

Each command runs once, prints plain text, and exits. No prompts, no loops.
"""

import os
import sys

# Make the engine package importable regardless of the working directory.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from engine.app import main

if __name__ == "__main__":
    main()
