"""The `help` verb: the one-screen command reference, grouped by context so the
list itself shows what's usable when. Rendered from the registry (single source
of truth), so it can never drift from what dispatch actually accepts."""

from ..render import paint, wordmark, cli, PAD
from .registry import VERBS


def cmd_help():
    print(wordmark("cyan"))
    print("")
    groups = (("anywhere", "always"), ("while solving a puzzle", "puzzle"))
    for i, (title, ctx) in enumerate(groups):
        if i:
            print("")                       # blank line between groups, not after
        print(PAD + paint(title, "magenta", "bold"))
        for _canon, label, _aliases, context, desc in VERBS:
            if context == ctx:
                # cli() owns the shell-aware form: bare `check` with the
                # shortcuts on, else `python3 start.py check`.
                print("%s%s  %s"
                      % (PAD, paint(cli(label).ljust(24), "green", "bold"),
                         desc))
