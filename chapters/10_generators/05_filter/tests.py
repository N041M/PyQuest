from engine.inputs import Case, random_int


def cases():
    cs = [Case(args=([1, 2, 3, 4],), expect=[2, 4]),
          Case(args=([1, 3, 5],), expect=[]),       # edge: none match
          Case(args=([],), expect=[]),              # edge: empty input
          Case(args=([2, 4, 6],), expect=[2, 4, 6]),  # edge: all match
          Case(args=([0, -2, -3],), expect=[0, -2])]  # edge: zero/negatives
    for _ in range(8):
        nums = [random_int(-9, 9) for _ in range(random_int(0, 8))]
        cs.append(Case(args=(nums,), expect=[n for n in nums if n % 2 == 0]))
    return cs


def check(T):
    for c in cases():
        gen = T.call("evens", *c.args)
        T.is_generator(gen,
                       because="evens must YIELD, so calling it returns a "
                               "generator -- not a finished list.")
        T.eq(list(gen), c.expect,
             because="evens(%r) should yield %r." % (c.args[0], c.expect))
    T.uses_yield("evens",
                 because="The lesson is a guarded yield: emit each even number "
                         "with yield behind an if in evens itself -- not a "
                         "returned list or a generator expression.")
