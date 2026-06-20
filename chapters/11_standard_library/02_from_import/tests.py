from math import gcd

from engine.inputs import Case, random_int


def cases():
    cs = [Case(args=(6, 8), expect=(3, 4)),
          Case(args=(10, 5), expect=(2, 1)),
          Case(args=(7, 7), expect=(1, 1))]
    for _ in range(8):
        g = random_int(1, 9)
        a, b = random_int(1, 12), random_int(1, 12)
        num, den = g * a, g * b
        h = gcd(num, den)
        cs.append(Case(args=(num, den), expect=(num // h, den // h)))
    return cs


def check(T):
    for c in cases():
        T.eq(T.call("simplify", *c.args), c.expect,
             because="simplify(%r, %r) reduces to %r" % (c.args + (c.expect,)))
    T.uses_import("math",
                  because="Reduce with gcd from the math module (from math "
                          "import gcd), not a hand-written gcd loop.")
