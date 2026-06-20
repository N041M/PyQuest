from engine.inputs import Case, random_word, random_int


def _expected(records, threshold):
    qualified = [r for r in records if r[1] >= threshold]
    ranked = sorted(qualified, key=lambda r: r[1], reverse=True)
    return [r[0] for r in ranked]


def cases():
    fixed = [("Ada", 90), ("Linus", 70), ("Grace", 95)]
    cs = [Case(args=(fixed, 80), expect=["Grace", "Ada"]),
          Case(args=([], 50), expect=[]),
          Case(args=(fixed, 100), expect=[])]
    for _ in range(8):
        records = [(random_word(3, 6), random_int(0, 100))
                   for _ in range(random_int(1, 7))]
        threshold = random_int(20, 80)
        cs.append(Case(args=(records, threshold),
                       expect=_expected(records, threshold)))
    return cs


def check(T):
    for c in cases():
        T.eq(T.call("passing", *c.args), c.expect,
             because="passing(%r, %r) -> %r" % (c.args + (c.expect,)))
    T.uses_call("filter",
                because="Select the qualifying records with filter(...).")
    T.uses_call("sorted",
                because="Rank them with sorted(..., key=lambda, reverse=True).")
    T.uses_lambda(because="Use lambdas for the filter test and the sort key.")
