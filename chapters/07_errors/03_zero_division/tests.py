from engine.inputs import Case, random_int


def cases():
    cs = [Case(args=(10, 4), expect=2.5),
          Case(args=(0, 5), expect=0.0),
          Case(args=(5, 0), expect=None),
          Case(args=(0, 0), expect=None)]
    for _ in range(8):
        a, b = random_int(-20, 20), random_int(0, 5)
        cs.append(Case(args=(a, b), expect=None if b == 0 else a / b))
    return cs


def check(T):
    for c in cases():
        got = T.call("safe_div", *c.args)
        if c.expect is None:
            T.true(got is None,
                   because="safe_div(%r, %r): dividing by zero should give "
                           "None." % c.args)
        else:
            T.approx(got, c.expect,
                     because="safe_div(%r, %r) should be %r." % (c.args[0],
                                                                 c.args[1],
                                                                 c.expect))
    T.uses_try(because="The lesson is EAFP -- catch ZeroDivisionError instead "
                       "of pre-testing b == 0.")
