import random

from engine.inputs import Case, random_int


def _expected(items, seed):
    out = list(items)
    random.seed(seed)
    random.shuffle(out)
    return out


def cases():
    cs = [Case(args=([], 1), expect=[]),
          Case(args=([42], 5), expect=[42])]
    for _ in range(8):
        items = [random_int(0, 99) for _ in range(random_int(2, 7))]
        seed = random_int(1, 10000)
        cs.append(Case(args=(items, seed), expect=_expected(items, seed)))
    return cs


def check(T):
    for c in cases():
        items, seed = c.args
        T.eq(T.call("shuffled", list(items), seed), c.expect,
             because="shuffled(%r, %r) must be the seed-%r shuffle of the items"
                     % (items, seed, seed))
    # the original list must survive untouched (shuffle a copy, not the input)
    original = [1, 2, 3, 4, 5]
    T.does_not_mutate("shuffled", original, 7)
    T.uses_import("random",
                  because="The order must come from random.shuffle with a seed -- "
                          "a hand-rolled reorder can't reproduce it.")
