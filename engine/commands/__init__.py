"""The command verbs, split by concern. This facade re-exports every cmd_* so
the dispatcher (app.py) imports from `engine.commands` exactly as before.

  registry.py   the command surface declared once: verb -> aliases, context
                (always / needs a puzzle), and help. app.py + help read it.
  cards.py      shared composition: the puzzle card, status marker, goto helpers
  views.py      read verbs (show, don't change position): status, map, stats,
                hint, solution, textbook
  navigate.py   navigation + workspace reset: goto, next, skip, retry, revert
  profiles.py   settings: theme, mode, user, reset
  transfer.py   export, import (portable profile bundles)
  shortcuts.py  the ~/.zshrc shortcuts installer (setup/persist/uninstall)
  help.py       help
  menu.py       the interactive launcher (menu)

`check` lives in checker.py; the dispatcher is app.py. See docs/ARCHITECTURE.md sec 4.
"""

from .views import (cmd_status, cmd_map, cmd_stats, cmd_hint, cmd_solution,
                    cmd_textbook)
from .navigate import cmd_goto, cmd_next, cmd_skip, cmd_retry, cmd_revert
from .profiles import cmd_theme, cmd_mode, cmd_user, cmd_reset
from .transfer import cmd_export, cmd_import
from .shortcuts import cmd_setup, cmd_setup_persist, cmd_uninstall
from .menu import cmd_menu
from .help import cmd_help

__all__ = [
    "cmd_status", "cmd_map", "cmd_stats", "cmd_hint", "cmd_solution",
    "cmd_textbook", "cmd_goto",
    "cmd_next", "cmd_skip", "cmd_retry", "cmd_revert", "cmd_mode",
    "cmd_theme", "cmd_user", "cmd_reset", "cmd_export", "cmd_import",
    "cmd_setup", "cmd_setup_persist", "cmd_uninstall",
    "cmd_menu", "cmd_help",
]
