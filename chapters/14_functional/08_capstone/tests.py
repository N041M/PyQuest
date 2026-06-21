import ast

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
    # Each pipeline stage must use a lambda in its role -- a decoy lambda parked
    # elsewhere while named functions (filter/sort) or a comprehension (map) do
    # the work no longer counts. Each call must also be live.
    def live_calls(name, pred):
        return [i for i, n in enumerate(ast.walk(T.tree()))
                if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                and n.func.id == name and pred(n)]

    def first_is_lambda(n):
        return bool(n.args) and isinstance(n.args[0], ast.Lambda)

    def key_is_lambda(n):
        return any(k.arg == "key" and isinstance(k.value, ast.Lambda)
                   for k in n.keywords)

    T.require_live("filter(lambda r: ..., records)",
                   "filter's predicate must be an inline lambda",
                   live_calls("filter", first_is_lambda), "expr",
                   because="Select the qualifying records with a filter lambda.")
    T.require_live("sorted(..., key=lambda r: ..., reverse=True)",
                   "the sort key must be an inline lambda",
                   live_calls("sorted", key_is_lambda), "expr",
                   because="Rank with sorted(..., key=lambda, reverse=True).")
    T.require_live("map(lambda r: r[0], ranked)",
                   "map out the names with a lambda, not a comprehension",
                   live_calls("map", first_is_lambda), "expr",
                   because="Map out the names with a lambda -- the map stage.")
