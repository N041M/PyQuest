from engine.inputs import random_int


def check(T):
    T.true(T.make("Money", 500) == T.make("Money", 500),
           because="same cents -> equal.")
    T.true(not (T.make("Money", 500) == T.make("Money", 750)),
           because="different cents -> not equal.")
    for _ in range(8):
        a, b = random_int(0, 9999), random_int(0, 9999)
        same = T.make("Money", a) == T.make("Money", a)
        T.true(same, because="Money(%d) should equal another Money(%d)." % (a, a))
        cmp = T.make("Money", a) == T.make("Money", b)
        T.eq(cmp, a == b,
             because="Money(%d) == Money(%d) should be %r." % (a, b, a == b))
    T.uses_class("Money", because="Money defines __eq__ for value equality.")
