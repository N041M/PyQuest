from engine.inputs import Case, random_int


def expected(n):
    if n < 0:
        return "negative"
    if n == 0:
        return "zero"
    return "positive"


def cases():
    cs = [Case(args=(n,), expect=expected(n))
          for n in (-3, 0, 42, -1, 1)]          # boundaries included
    for _ in range(8):
        n = random_int(-40, 40)
        cs.append(Case(args=(n,), expect=expected(n)))
    return cs


def check(T):
    for c in cases():
        T.eq(T.call("sign", *c.args), c.expect,
             because="sign(%r) should return %r." % (c.args[0], c.expect))
