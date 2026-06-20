from collections import Counter

from engine.inputs import Case, random_int


def cases():
    cs = [Case(args=(["a", "b", "a"],), expect={"a": 2, "b": 1}),
          Case(args=([],), expect={})]
    alphabet = ["a", "b", "c", "d"]
    for _ in range(8):
        items = [alphabet[random_int(0, 3)] for _ in range(random_int(1, 12))]
        cs.append(Case(args=(items,), expect=dict(Counter(items))))
    return cs


def check(T):
    for c in cases():
        T.eq(T.call("tally", *c.args), c.expect,
             because="tally(%r) counts each item -> %r" % (c.args[0], c.expect))
    T.uses_import("collections",
                  because="Count with Counter from collections, not a hand-built "
                          "dict loop.")
    T.uses_call("Counter",
                because="The lesson is Counter specifically -- use it to tally.")
