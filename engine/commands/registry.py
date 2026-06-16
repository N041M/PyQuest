"""The command surface, declared once. This is the single source of truth for
what verbs exist, what each is called (aliases), which context each needs, and
its one-line help. `app.py` canonicalizes + gates + suggests from here; `help`
renders from here. Add a verb in exactly two places: a row here and its handler
in `app.main()`.

context:
  "always"  usable any time (navigation, settings, profiles, the menu)
  "puzzle"  only meaningful with a puzzle loaded into work.py; without one,
            dispatch redirects the learner to `begin`/`goto` instead of running
            a verb that has nothing to act on.

Each row: (canonical, label, aliases, context, help)
  canonical  the dispatch key app.main() switches on
  label      how the verb prints in `help` (may carry an argument placeholder)
"""

VERBS = [
    ("begin",     "begin",        (),                "always",
     "open the main menu (start here)"),
    ("menu",      "menu",         ("back",),         "always",
     "leave the puzzle and return to the main menu"),
    ("status",    "status",       ("current", "progress"), "always",
     "show progress and the current puzzle"),
    ("map",       "map",          (),                "always",
     "show the chapter/puzzle tree"),
    ("lexicon",   "lexicon",      ("ref",),          "always",
     "syntax & tips you've reached (lexicon all for the full reference)"),
    ("check",     "check",        (),                "puzzle",
     "validate your work.py"),
    ("hint",      "hint",         (),                "puzzle",
     "reveal the next hint"),
    ("solution",  "solution",     (),                "puzzle",
     "show the reference solution"),
    ("next",      "next",         (),                "puzzle",
     "move on to the next puzzle"),
    ("skip",      "skip",         (),                "puzzle",
     "move on without solving the current puzzle"),
    ("retry",     "retry",        ("replay",),       "puzzle",
     "blank the workspace to practice again (stays solved)"),
    ("revert",    "revert",       (),                "puzzle",
     "fully reset this puzzle: blank code + clear its progress"),
    ("goto",      "goto <id>",    ("load",),         "always",
     "jump to a puzzle (goto 2.4, or goto 2 for chapter 2; bare opens a picker)"),
    ("mode",      "mode <m>",     (),                "always",
     "set difficulty: easy | normal | hard"),
    ("theme",     "theme <name>", (),                "always",
     "switch colour theme (neon, amber, forest, mono)"),
    ("user",      "user <name>",  ("users",),        "always",
     "switch or create a profile"),
    ("export",    "export",       (),                "always",
     "save this profile's progress to a portable file"),
    ("import",    "import <file>", (),               "always",
     "load a profile from an exported file"),
    ("reset",     "reset",        (),                "always",
     "wipe progress, saved answers, and workspaces"),
    ("setup",     "setup",        (),                "always",
     "set up the short commands (offers local or persistent)"),
    ("uninstall", "uninstall",    (),                "always",
     "remove the persistent shortcuts"),
    ("help",      "help",         ("-h", "--help"),  "always",
     "show this command list"),
]

CANONICAL = {row[0] for row in VERBS}
ALIASES = {alias: row[0] for row in VERBS for alias in row[2]}
NEEDS_PUZZLE = {row[0] for row in VERBS if row[3] == "puzzle"}

# Which verbs appear in the shared bottom nav strip, in clusters and order.
# `check`/`next`/`begin` are not listed: they surface as the highlighted primary
# chip instead (chosen from state in cards.nav_strip). Verbs omitted entirely
# (export/import/setup/uninstall/reset) stay discoverable via `help`/`menu`, not
# the strip. This keeps the strip the single source of truth for navigation
# while staying terse. Puzzle-only verbs are filtered out when no puzzle loaded.
NAV_CLUSTERS = [
    ("learn", ("hint", "solution")),
    ("move",  ("map", "goto", "next", "skip")),
    ("do",    ("retry", "revert")),
    ("set",   ("mode", "theme", "user")),
]


def canonical(cmd):
    """Map an alias (or empty input) to its canonical verb; pass others through."""
    if not cmd:
        return "status"
    return ALIASES.get(cmd, cmd)


def _all_names():
    names = []
    for row in VERBS:
        names.append(row[0])
        names.extend(row[2])
    return names


def suggest(cmd):
    """The closest known verb to a mistyped command, or None. Used for the
    'did you mean?' hint on an unknown command."""
    import difflib
    match = difflib.get_close_matches(cmd, _all_names(), n=1, cutoff=0.6)
    return canonical(match[0]) if match else None
