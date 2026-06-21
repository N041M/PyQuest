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
    # filter must do the selecting over the INPUT, not wrap a comprehension that
    # already kept the evens (filter(lambda v: True, [...]) doesn't count).
    T.uses_call_over_param("filter",
                           because="Select the evens with filter(...) over the "
                                   "input -- the lesson is filter, not a "
                                   "comprehension or manual loop.")
