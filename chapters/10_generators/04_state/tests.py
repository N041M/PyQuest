from engine.inputs import Case, random_int


def running(nums):
    total = 0
    out = []
    for n in nums:
        total += n
        out.append(total)
    return out


def cases():
    cs = [Case(args=([3, 1, 2],), expect=[3, 4, 6]),
          Case(args=([5],), expect=[5]),
          Case(args=([],), expect=[]),          # edge: nothing to yield
          Case(args=([2, -2, 3],), expect=[2, 0, 3])]   # edge: negatives
    for _ in range(8):
        nums = [random_int(-9, 9) for _ in range(random_int(0, 7))]
        cs.append(Case(args=(nums,), expect=running(nums)))
    return cs


def check(T):
    for c in cases():
        gen = T.call("running_total", *c.args)
        T.is_generator(gen,
                       because="running_total must YIELD, so calling it returns "
                               "a generator -- not a finished list of totals.")
        T.eq(list(gen), c.expect,
             because="running_total(%r) should yield %r."
                     % (c.args[0], c.expect))
    T.uses_yield("running_total",
                 because="The lesson is state across yields: keep a total in a "
                         "variable and yield it in running_total itself -- not "
                         "a returned list or a generator expression.")
