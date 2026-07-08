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

import os
import random
import string


# The seed in effect for this run, recorded so any run can be replayed.
ACTIVE_SEED = None


def init_seed(env=None):
    """Seed the global RNG and record the seed in ACTIVE_SEED. If PYQUEST_SEED is
    set, use it; otherwise pick a fresh random seed -- either way the seed is
    RECORDED, so a run (a `check`, or a full `audit.py`) can be replayed exactly
    with `PYQUEST_SEED=<seed>`. Fresh randomness each run is still what defeats
    hardcoding; recording it just makes a failure reproducible instead of lost.
    Returns the seed used (int, or the raw string for a non-integer override)."""
    global ACTIVE_SEED
    env = os.environ if env is None else env
    raw = env.get("PYQUEST_SEED")
    if raw is None:
        seed = random.randrange(2 ** 31)
    else:
        try:
            seed = int(raw)
        except ValueError:
            seed = raw
    random.seed(seed)
    ACTIVE_SEED = seed
    return seed


init_seed()


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


# ---- convenience generators used by tests.py to defeat hardcoding ----------
def random_word(min_len=3, max_len=8, rng=None):
    """A random lowercase word."""
    rng = rng or random
    n = rng.randint(min_len, max_len)
    return "".join(rng.choice(string.ascii_lowercase) for _ in range(n))


def random_int(low, high, rng=None):
    """A single random integer in [low, high]."""
    return (rng or random).randint(low, high)
