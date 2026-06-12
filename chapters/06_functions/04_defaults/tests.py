from engine.inputs import Case, random_word


def cases():
    cs = [Case(args=("Ada",), expect="Hello, Ada!",
               meta={"note": "the default greeting"}),
          Case(args=("Ada", "Hi"), expect="Hi, Ada!")]
    for _ in range(4):
        n = random_word(2, 8)
        cs.append(Case(args=(n,), expect="Hello, %s!" % n))
    for _ in range(4):
        n, g = random_word(2, 8), random_word(2, 6)
        cs.append(Case(args=(n, g), expect="%s, %s!" % (g, n)))
    return cs


def check(T):
    for c in cases():
        T.eq(T.call("greet", *c.args), c.expect, match_case=True,
             because="greet%r should return %r -- called with %d argument(s)."
                     % (c.args, c.expect, len(c.args)))
