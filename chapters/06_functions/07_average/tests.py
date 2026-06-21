from engine.inputs import Case, random_int


def cases():
    cs = [Case(args=([1, 2],), expect=1.5),
          Case(args=([10, 20, 30],), expect=20.0),
          Case(args=([7],), expect=7.0)]
    for _ in range(8):
        nums = [random_int(-20, 20) for _ in range(random_int(1, 8))]
        cs.append(Case(args=(nums,), expect=sum(nums) / len(nums)))
    return cs


def check(T):
    exact = T.call("average", [10, 20, 30])
    T.is_a(exact, float,
           because="/ always returns a float -- 60 / 3 is 20.0, not 20. "
                   "(// would throw the decimals away.)")
    for c in cases():
        T.approx(T.call("average", *c.args), c.expect,
                 because="average(%r) should be %r." % (c.args[0], c.expect))
    T.uses_call_over_param("sum",
                           because="The lesson is bundling the built-ins "
                                   "(sum(nums) / len(nums)) over the input -- a "
                                   "hand-written accumulator loop, even wrapped "
                                   "in sum([total]), is the long way this puzzle "
                                   "replaces.")
