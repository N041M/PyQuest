from collections import defaultdict

from engine.inputs import Case, random_word, random_int


def _expected(words):
    groups = defaultdict(list)
    for w in words:
        groups[len(w)].append(w)
    return dict(groups)


def cases():
    cs = [Case(args=(["hi", "ok", "bye"],), expect={2: ["hi", "ok"], 3: ["bye"]}),
          Case(args=([],), expect={})]
    for _ in range(8):
        words = [random_word(2, 7) for _ in range(random_int(2, 8))]
        cs.append(Case(args=(words,), expect=_expected(words)))
    return cs


def check(T):
    for c in cases():
        T.eq(T.call("group_by_length", *c.args), c.expect,
             because="group_by_length(%r) groups by length -> %r"
                     % (c.args[0], c.expect))
    T.uses_import("collections",
                  because="Group with a defaultdict from collections, not a "
                          "manual 'if key not in dict' setup.")
    T.uses_call("defaultdict",
                because="The lesson is defaultdict specifically -- use it to "
                        "auto-create each group's list.")
