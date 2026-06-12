from engine.inputs import Case, random_int


def cases():
    cs = [Case(args=(3,), expect=6),
          Case(args=(0,), expect=0),
          Case(args=(-5,), expect=-10)]
    for _ in range(8):
        x = random_int(-50, 50)
        cs.append(Case(args=(x,), expect=x * 2))
    return cs


def check(T):
    for c in cases():
        T.eq(T.call("double", *c.args), c.expect,
             because="double(%r) should return %r." % (c.args[0], c.expect))
