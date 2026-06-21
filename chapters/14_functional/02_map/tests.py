import ast

from engine.inputs import Case, random_int


def _params(T):
    """Names of every def's parameters -- the input the HOF must iterate."""
    return {a.arg for f in ast.walk(T.tree())
            if isinstance(f, ast.FunctionDef) for a in f.args.args}


def cases():
    cs = [Case(args=([1, 2, 3],), expect=[1, 4, 9]),
          Case(args=([],), expect=[])]
    for _ in range(8):
        nums = [random_int(-20, 20) for _ in range(random_int(1, 6))]
        cs.append(Case(args=(nums,), expect=[x * x for x in nums]))
    return cs


def check(T):
    for c in cases():
        T.eq(T.call("squares", *c.args), c.expect,
             because="squares(%r) -> %r" % (c.args[0], c.expect))
    T.uses_call("map",
                because="Apply the squaring with map(...), not a comprehension or "
                        "manual loop -- the lesson is map.")
    # map must do the transform over the INPUT, not wrap a comprehension that
    # already squared: require a live map(func, nums) whose iterable is the
    # parameter, so map(lambda v: v, [x * x for x in nums]) no longer counts.
    params = _params(T)
    live = [i for i, n in enumerate(ast.walk(T.tree()))
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
            and n.func.id == "map" and len(n.args) >= 2
            and isinstance(n.args[1], ast.Name) and n.args[1].id in params]
    T.require_live("map(func, nums) applied to the input itself",
                   "map must do the squaring over the input list, not wrap a "
                   "comprehension that already computed the squares",
                   live, "expr",
                   because="The lesson is map performing the transform.")
