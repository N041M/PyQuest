from engine.inputs import Case, random_int


def cases():
    cs = [Case(args=(3, 4), expect=12),
          Case(args=(5, 0), expect=0),
          Case(args=(1, 7), expect=7)]
    for _ in range(8):
        w, h = random_int(0, 30), random_int(0, 30)
        cs.append(Case(args=(w, h), expect=w * h))
    return cs


def check(T):
    for c in cases():
        T.eq(T.call("rect_area", *c.args), c.expect,
             because="rect_area(%r, %r) should return %r."
                     % (c.args[0], c.args[1], c.expect))
