from engine.inputs import Case, random_int


def cases():
    cs = [Case(args=([1, 2, 3],), expect=True),
          Case(args=([1, -2, 3],), expect=False),
          Case(args=([],), expect=True)]
    for _ in range(8):
        nums = [random_int(-15, 15) for _ in range(random_int(1, 7))]
        cs.append(Case(args=(nums,), expect=all(n > 0 for n in nums)))
    return cs


def check(T):
    for c in cases():
        T.eq(T.call("all_positive", *c.args), c.expect,
             because="all_positive(%r) -> %r" % (c.args[0], c.expect))
    # all() must consume a comprehension/genexpr over the INPUT -- the taught
    # all(<test> for <item> in nums) pattern. A loop-with-a-flag whose result is
    # wrapped in all([flag]) or all(flag for _ in [0]) doesn't iterate the input.
    T.uses_predicate_over_param("all",
                                because="Use all(<test> for <item> in nums), "
                                        "not a loop-with-a-flag.")
