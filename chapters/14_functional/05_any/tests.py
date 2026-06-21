import ast

from engine.inputs import Case, random_int

_COMPS = (ast.GeneratorExp, ast.ListComp, ast.SetComp)


def _params(T):
    return {a.arg for f in ast.walk(T.tree())
            if isinstance(f, ast.FunctionDef) for a in f.args.args}


def cases():
    cs = [Case(args=([1, 2, -3],), expect=True),
          Case(args=([1, 2, 3],), expect=False),
          Case(args=([],), expect=False)]
    for _ in range(8):
        nums = [random_int(-15, 15) for _ in range(random_int(1, 7))]
        cs.append(Case(args=(nums,), expect=any(n < 0 for n in nums)))
    return cs


def check(T):
    for c in cases():
        T.eq(T.call("has_negative", *c.args), c.expect,
             because="has_negative(%r) -> %r" % (c.args[0], c.expect))
    T.uses_call("any",
                because="Use any(...), not a loop-with-a-flag -- the lesson is "
                        "any.")
    # any() must consume a comprehension/genexpr over the INPUT -- the taught
    # pattern any(<test> for <item> in nums). A loop-with-a-flag whose result is
    # wrapped in any([flag]) or any(flag for _ in [0]) does not iterate the
    # input, so neither counts.
    params = _params(T)

    def over_input(n):
        return (isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                and n.func.id == "any" and n.args
                and isinstance(n.args[0], _COMPS) and n.args[0].generators
                and isinstance(n.args[0].generators[0].iter, ast.Name)
                and n.args[0].generators[0].iter.id in params)

    live = [i for i, n in enumerate(ast.walk(T.tree())) if over_input(n)]
    T.require_live("any(<test> for <item> in nums)",
                   "hand the per-item tests to any() as a comprehension over "
                   "the input, not a flag a loop precomputed",
                   live, "expr",
                   because="The lesson is any over the input, not a "
                           "loop-with-a-flag wrapped in any().")
