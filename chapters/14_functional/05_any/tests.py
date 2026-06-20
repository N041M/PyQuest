from engine.inputs import Case, random_int


def cases():
    cs = [Case(args=([1, 2, -3],), expect=True),
          Case(args=([1, 2, 3],), expect=False),
          Case(args=([],), expect=False)]
    for _ in range(8):
        nums = [random_int(-15, 15) for _ in range(random_int(1, 7))]
        cs.append(Case(args=(nums,), expect=any(n < 0 for n in nums)))
    return cs


def check(T):
    for c in cases():
        T.eq(T.call("has_negative", *c.args), c.expect,
             because="has_negative(%r) -> %r" % (c.args[0], c.expect))
    T.uses_call("any",
                because="Use any(...), not a loop-with-a-flag -- the lesson is "
                        "any.")
