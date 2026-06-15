"""The command verbs, split by concern. This facade re-exports every cmd_* so
the dispatcher (app.py) imports from `engine.commands` exactly as before.

  cards.py      shared composition: the puzzle card, status marker, goto helpers
  play.py       loop verbs: status, map, hint, solution, goto, next, skip,
                retry, revert, mode
  profiles.py   theme, user, reset
  shortcuts.py  the ~/.zshrc shortcuts installer (setup/persist/uninstall)
  help.py       help
  menu.py       the interactive launcher (begin / menu)

`check` lives in checker.py; the dispatcher is app.py. See docs/ARCHITECTURE.md sec 4.
"""

from .play import (cmd_status, cmd_map, cmd_hint, cmd_solution, cmd_goto,
                   cmd_next, cmd_skip, cmd_retry, cmd_revert, cmd_mode)
from .profiles import cmd_theme, cmd_user, cmd_reset
from .shortcuts import cmd_setup, cmd_setup_persist, cmd_uninstall
from .menu import cmd_begin, cmd_menu
from .help import cmd_help

__all__ = [
    "cmd_status", "cmd_map", "cmd_hint", "cmd_solution", "cmd_goto",
    "cmd_next", "cmd_skip", "cmd_retry", "cmd_revert", "cmd_mode",
    "cmd_theme", "cmd_user", "cmd_reset",
    "cmd_setup", "cmd_setup_persist", "cmd_uninstall",
    "cmd_begin", "cmd_menu", "cmd_help",
]
