"""The `help` verb: the one-screen command reference, grouped by context so the
list itself shows what's usable when. Rendered from the registry (single source
of truth), so it can never drift from what dispatch actually accepts."""

import os

from ..render import paint, wordmark, PAD
from .registry import VERBS


def cmd_help():
    print(wordmark("cyan"))
    print("")
    # With the shortcuts on, verbs are bare; otherwise show the full invocation.
    pre = "" if os.environ.get("PYQUEST_SHELL") else "python3 start.py "
    for title, ctx in (("anywhere", "always"),
                       ("while solving a puzzle", "puzzle")):
        print(PAD + paint(title, "magenta", "bold"))
        for _canon, label, _aliases, context, desc in VERBS:
            if context == ctx:
                print("%s%s  %s"
                      % (PAD, paint((pre + label).ljust(24), "green", "bold"),
                         desc))
        print("")
