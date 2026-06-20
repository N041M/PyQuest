from engine.inputs import Case, random_int


def cases():
    cs = [Case(args=([1, 2, 3, 4],), expect=[2, 4]),
          Case(args=([1, 3, 5],), expect=[])]
    for _ in range(8):
        nums = [random_int(-30, 30) for _ in range(random_int(1, 8))]
        cs.append(Case(args=(nums,), expect=[x for x in nums if x % 2 == 0]))
    return cs


def check(T):
    for c in cases():
        T.eq(T.call("evens", *c.args), c.expect,
             because="evens(%r) -> %r" % (c.args[0], c.expect))
    T.uses_call("filter",
                because="Select the evens with filter(...), not a comprehension "
                        "or manual loop -- the lesson is filter.")
