from engine.inputs import Case, random_int


def cases():
    cs = [Case(args=([3, 1, 4],), expect=(1, 4)),
          Case(args=([7],), expect=(7, 7)),
          Case(args=([-2, -9, 0],), expect=(-9, 0))]
    for _ in range(8):
        nums = [random_int(-30, 30) for _ in range(random_int(1, 7))]
        cs.append(Case(args=(nums,), expect=(min(nums), max(nums))))
    return cs


def check(T):
    for c in cases():
        got = T.call("min_max", *c.args)
        T.is_a(got, tuple,
               because="Two comma-separated returned values arrive as a tuple.")
        T.eq(got, c.expect,
             because="min_max(%r) should return %r -- smallest first."
                     % (c.args[0], c.expect))
