from engine.inputs import Case, random_int


def cases():
    cs = [Case(args=([1, 2, 3],), expect=[1, 4, 9]),
          Case(args=([],), expect=[])]
    for _ in range(8):
        nums = [random_int(-20, 20) for _ in range(random_int(1, 6))]
        cs.append(Case(args=(nums,), expect=[x * x for x in nums]))
    return cs


def check(T):
    for c in cases():
        T.eq(T.call("squares", *c.args), c.expect,
             because="squares(%r) -> %r" % (c.args[0], c.expect))
    T.uses_call("map",
                because="Apply the squaring with map(...), not a comprehension or "
                        "manual loop -- the lesson is map.")
