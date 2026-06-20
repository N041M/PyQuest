from engine.inputs import Case, random_int


def cases():
    cs = [Case(args=(3, 4), expect=5.0),
          Case(args=(5, 12), expect=13.0),
          Case(args=(0, 0), expect=0.0)]
    for _ in range(8):
        a, b = random_int(1, 40), random_int(1, 40)
        cs.append(Case(args=(a, b), expect=(a * a + b * b) ** 0.5))
    return cs


def check(T):
    for c in cases():
        T.approx(T.call("hypotenuse", *c.args), c.expect,
                 because="hypotenuse(%r, %r) is sqrt(a*a + b*b) = %r"
                         % (c.args[0], c.args[1], c.expect))
    T.uses_import("math",
                  because="Use the math module (math.sqrt), not ** 0.5 -- the "
                          "lesson is importing and using the standard library.")
