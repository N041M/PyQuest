"""The `help` verb: the one-screen command reference, grouped by the two command
sets (puzzle logic vs anywhere) and highlighted for the current space -- the
verbs you can use right now are bright with a ▸; the rest are dimmed with a ·.
Rendered from the registry (single source of truth), so it can never drift from
what dispatch actually accepts."""

from ..render import paint, wordmark, cli, PAD, CUR, DOT
from ..i18n import t
from .registry import VERBS


def cmd_help(prog):
    active = bool(prog.get("active"))
    print(wordmark("cyan"))
    print("")
    where = (t("help.in_puzzle", "in puzzle %s") % prog.get("current")) if active \
        else t("help.no_loaded", "no puzzle loaded")
    print(PAD + paint(t("help.title", "command reference"), "magenta", "bold")
          + paint("   (%s)" % where, "gray"))
    print("")
    # The current space first: the puzzle set is live only while solving.
    groups = ((t("help.group_puzzle", "while solving a puzzle"), "puzzle"),
              (t("help.group_always", "anywhere"), "always"))
    for i, (title, ctx) in enumerate(groups):
        if i:
            print("")                       # blank line between groups, not after
        live = active or ctx == "always"
        note = (t("help.available_now", "available now") if live
                else t("help.load_first", "load a puzzle first (%s)")
                % cli("menu"))
        print(PAD + paint(title, "magenta", "bold")
              + paint("   %s" % note, "green" if live else "gray"))
        for _canon, label, _aliases, context, desc in VERBS:
            if context != ctx:
                continue
            avail = active or context == "always"
            desc = t("help.desc." + _canon, desc)
            # cli() owns the shell-aware form: bare `check` with the shortcuts
            # on, else `python3 start.py check`.
            if avail:
                row = "%s %s  %s" % (paint(CUR, "green", "bold"),
                                     paint(cli(label).ljust(24), "green", "bold"),
                                     desc)
            else:
                row = "%s %s  %s" % (paint(DOT, "gray"),
                                     paint(cli(label).ljust(24), "gray"),
                                     paint(desc, "gray"))
            print(PAD + row)
    print("")
    print(PAD + paint(t("help.footer",
                      "%s available now   %s needs a puzzle loaded")
                      % (CUR, DOT), "gray"))
