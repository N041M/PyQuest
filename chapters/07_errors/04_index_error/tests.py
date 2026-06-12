from engine.inputs import Case, random_word, random_int


def cases():
    base = ["a", "b"]
    cs = [Case(args=(base, 0, "?"), expect="a"),
          Case(args=(base, 1, "?"), expect="b"),
          Case(args=(base, -1, "?"), expect="b"),
          Case(args=(base, -2, "?"), expect="a"),
          Case(args=(base, 5, "?"), expect="?"),
          Case(args=(base, -3, "?"), expect="?"),
          Case(args=([], 0, "?"), expect="?")]
    for _ in range(8):
        items = [random_word(1, 4) for _ in range(random_int(0, 5))]
        i = random_int(-7, 7)
        ok = -len(items) <= i < len(items)
        cs.append(Case(args=(items, i, "fallback"),
                       expect=items[i] if ok else "fallback"))
    return cs


def check(T):
    for c in cases():
        T.eq(T.call("item_or", *c.args), c.expect,
             because="item_or(%r, %r, %r) should be %r." % (c.args[0],
                                                            c.args[1],
                                                            c.args[2],
                                                            c.expect))
    T.uses_try(because="The lesson is catching IndexError -- let Python "
                       "decide which indexes are bad.")
