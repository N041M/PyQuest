from engine.inputs import random_word, random_int


def check(T):
    T.eq(T.call("safe_int", "42"), 42)
    T.eq(T.call("safe_int", "-7"), -7)
    T.true(T.call("safe_int", "nope") is None,
           because="Unconvertible text returns None, not a crash.")
    T.true(T.call("safe_int", "") is None,
           because="An empty string is not a number either.")
    for _ in range(6):
        if random_int(0, 1):
            n = random_int(-99, 99)
            T.eq(T.call("safe_int", "%d" % n), n,
                 because="safe_int(%r)." % ("%d" % n))
        else:
            w = random_word(2, 8)
            T.true(T.call("safe_int", w) is None,
                   because="safe_int(%r) should be None." % w)
    T.raises(TypeError, "safe_int", [1, 2])
    T.uses_try(because="Handle the ValueError with try/except.")
