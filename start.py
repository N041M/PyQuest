#!/usr/bin/env python3
"""PyQuest, the one entry point.

    python3 start.py            set up the session shortcuts and open the menu
    python3 start.py <command>  run a single command (check, hint, next, ...)

This file only routes: it checks your Python, then either hosts a session
(`engine.session`) for a cold, bare launch, or dispatches one command
(`engine.app`). Given a verb -- or run from inside an already-set-up session
(PYQUEST_SHELL) -- it dispatches; only a cold bare run sets up a new session.
"""

import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)                   # make the engine package importable
MIN_PY = (3, 8)


def main():
    if sys.version_info < MIN_PY:
        sys.stderr.write(
            "PyQuest needs Python %d.%d or newer; this is Python %d.%d.\n"
            "Get a newer Python 3 from https://www.python.org/downloads/.\n"
            % (MIN_PY[0], MIN_PY[1], sys.version_info[0], sys.version_info[1]))
        return 1

    if sys.argv[1:] or os.environ.get("PYQUEST_SHELL"):
        from engine.app import main as run
        run()
        return 0

    from engine.session import launch_session
    return launch_session()


if __name__ == "__main__":
    sys.exit(main())
