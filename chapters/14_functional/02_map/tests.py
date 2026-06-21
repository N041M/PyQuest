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
    # map must do the squaring over the INPUT, not wrap a comprehension that
    # already computed it (map(lambda v: v, [x * x for x in nums]) doesn't count).
    T.uses_call_over_param("map",
                           because="Apply the squaring with map(...) over the "
                                   "input -- the lesson is map, not a "
                                   "comprehension or manual loop.")
