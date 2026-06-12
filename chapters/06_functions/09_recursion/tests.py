from engine.inputs import Case, random_int


def fact(n):
    out = 1
    for i in range(2, n + 1):
        out *= i
    return out


def cases():
    cs = [Case(args=(0,), expect=1),
          Case(args=(1,), expect=1),
          Case(args=(5,), expect=120)]
    for _ in range(6):
        n = random_int(2, 10)
        cs.append(Case(args=(n,), expect=fact(n)))
    return cs


def check(T):
    for c in cases():
        T.eq(T.call("fact", *c.args), c.expect,
             because="fact(%r) should return %r." % (c.args[0], c.expect))
    T.uses_call("fact", because="The lesson is recursion -- fact must call "
                                "itself (a loop computes the value but dodges "
                                "the concept).")
