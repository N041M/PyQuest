from engine.inputs import Case, random_int


def until(nums):
    out = []
    for n in nums:
        if n == 0:
            break
        out.append(n)
    return out


def cases():
    cs = [Case(args=([1, 2, 0, 3],), expect=[1, 2]),
          Case(args=([0, 9],), expect=[]),          # edge: 0 first -> empty
          Case(args=([1, 2, 3],), expect=[1, 2, 3]),  # edge: no 0 -> all
          Case(args=([],), expect=[]),              # edge: empty input
          Case(args=([5, 0, 0],), expect=[5])]      # edge: trailing zeros gone
    for _ in range(8):
        nums = [random_int(0, 4) for _ in range(random_int(0, 8))]
        cs.append(Case(args=(nums,), expect=until(nums)))
    return cs


def check(T):
    for c in cases():
        gen = T.call("until_zero", *c.args)
        T.is_generator(gen,
                       because="until_zero must YIELD, so calling it returns a "
                               "generator -- not a finished list.")
        T.eq(list(gen), c.expect,
             because="until_zero(%r) should yield %r." % (c.args[0], c.expect))
    T.uses_yield("until_zero",
                 because="The lesson is yielding then stopping early: emit each "
                         "number with yield and return at the first 0, in "
                         "until_zero itself -- not a returned slice or a "
                         "generator expression.")
