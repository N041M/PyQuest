import ast

from engine.inputs import Case, random_int


def _params(T):
    """Names of every def's parameters -- the input the HOF must iterate."""
    return {a.arg for f in ast.walk(T.tree())
            if isinstance(f, ast.FunctionDef) for a in f.args.args}


def cases():
    cs = [Case(args=([1, 2, 3, 4],), expect=[2, 4]),
          Case(args=([1, 3, 5],), expect=[])]
    for _ in range(8):
        nums = [random_int(-30, 30) for _ in range(random_int(1, 8))]
        cs.append(Case(args=(nums,), expect=[x for x in nums if x % 2 == 0]))
    return cs


def check(T):
    for c in cases():
        T.eq(T.call("evens", *c.args), c.expect,
             because="evens(%r) -> %r" % (c.args[0], c.expect))
    T.uses_call("filter",
                because="Select the evens with filter(...), not a comprehension "
                        "or manual loop -- the lesson is filter.")
    # filter must select over the INPUT, not wrap a comprehension that already
    # selected: require a live filter(pred, nums) whose iterable is the
    # parameter, so filter(lambda v: True, [x for x in nums if ...]) is out.
    params = _params(T)
    live = [i for i, n in enumerate(ast.walk(T.tree()))
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
            and n.func.id == "filter" and len(n.args) >= 2
            and isinstance(n.args[1], ast.Name) and n.args[1].id in params]
    T.require_live("filter(pred, nums) applied to the input itself",
                   "filter must do the selecting over the input list, not wrap "
                   "a comprehension that already kept the evens",
                   live, "expr",
                   because="The lesson is filter performing the selection.")
