from engine.inputs import random_int


def check(T):
    ns = [3, 10, 0, -2] + [random_int(-12, 12) for _ in range(5)]
    for n in ns:
        fn = T.call("multiplier", n)
        T.true(callable(fn),
               because="multiplier(%r) should RETURN a function." % n)
        for x in [4, 0, -5] + [random_int(-20, 20) for _ in range(3)]:
            T.eq(fn(x), n * x,
                 because="multiplier(%r)(%r) should be %r" % (n, x, n * x))
    # The returned function must itself be the lambda -- a nested def carries its
    # own name, a lambda is named "<lambda>". This anchors the lesson to the
    # value multiplier returns, so a decoy lambda parked elsewhere (which would
    # satisfy the bare uses_lambda below) cannot stand in for a nested def.
    fn = T.call("multiplier", 3)
    T.true(getattr(fn, "__name__", "") == "<lambda>",
           because="multiplier must RETURN a lambda, not a nested def.")
    T.uses_lambda(because="Return an inline lambda, not a nested def.")
