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
    T.uses_lambda(because="Return an inline lambda, not a nested def.")
