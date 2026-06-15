"""Input providers -- the 'input automizer' seam.

A provider supplies one or more *cases*. A case bundles what the solution
receives (stdin / call args) with the data the checker needs to compute the
expected result, so a single source decides both the input and the validation.

The `random_word` / `random_int` generators below are used by the input-reading
puzzles in Chapters 1-2 (and beyond): their tests.py feed randomized stdin and
compute the expected result, so the answer cannot be hardcoded. The `Case` /
structured-provider shape is live in the import-mode puzzles of Chapter 6+:
tests build fixed + randomized Cases, feed case.args to T.call, and validate
against case.expect.
"""

import random
import string


class Case:
    """One input case for a puzzle.

    stdin   : text fed to a script-mode solution's input()
    args    : positional args for an import-mode function call
    kwargs  : keyword args for the call
    expect  : the expected result (or a key the checker uses to compute it)
    meta    : anything else the checker/brief wants to know about this case
    """

    def __init__(self, stdin="", args=(), kwargs=None, expect=None, meta=None):
        self.stdin = stdin
        self.args = tuple(args)
        self.kwargs = dict(kwargs or {})
        self.expect = expect
        self.meta = dict(meta or {})

    def __repr__(self):
        return "Case(stdin=%r, args=%r, expect=%r)" % (
            self.stdin, self.args, self.expect)


def fixed(*cases):
    """A provider of predetermined cases."""
    return list(cases)


# ---- convenience generators used by tests.py to defeat hardcoding ----------
def random_word(min_len=3, max_len=8, rng=None):
    """A random lowercase word."""
    rng = rng or random
    n = rng.randint(min_len, max_len)
    return "".join(rng.choice(string.ascii_lowercase) for _ in range(n))


def random_int(low, high, rng=None):
    """A single random integer in [low, high]."""
    return (rng or random).randint(low, high)
