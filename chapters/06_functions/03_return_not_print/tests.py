from engine.inputs import Case, random_word


def cases():
    cs = [Case(args=("hi",), expect="HI!"),
          Case(args=("",), expect="!")]
    for _ in range(8):
        w = random_word(1, 9)
        cs.append(Case(args=(w,), expect=w.upper() + "!"))
    return cs


def check(T):
    for c in cases():
        got = T.call("shout", *c.args)
        T.true(got is not None,
               because="shout(%r) returned None -- did it print instead of "
                       "return? The caller must RECEIVE the value." % (c.args[0],))
        T.eq(got, c.expect, match_case=True,
             because="shout(%r) should return %r." % (c.args[0], c.expect))
