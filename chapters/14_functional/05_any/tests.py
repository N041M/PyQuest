from engine.inputs import Case, random_int


def cases():
    cs = [Case(args=([1, 2, -3],), expect=True),
          Case(args=([1, 2, 3],), expect=False),
          Case(args=([],), expect=False)]
    for _ in range(8):
        nums = [random_int(-15, 15) for _ in range(random_int(1, 7))]
        cs.append(Case(args=(nums,), expect=any(n < 0 for n in nums)))
    return cs


def check(T):
    for c in cases():
        T.eq(T.call("has_negative", *c.args), c.expect,
             because="has_negative(%r) -> %r" % (c.args[0], c.expect))
    # any() must consume a comprehension/genexpr over the INPUT -- the taught
    # any(<test> for <item> in nums) pattern. A loop-with-a-flag whose result is
    # wrapped in any([flag]) or any(flag for _ in [0]) doesn't iterate the input.
    T.uses_predicate_over_param("any",
                                because="Use any(<test> for <item> in nums), "
                                        "not a loop-with-a-flag.")
