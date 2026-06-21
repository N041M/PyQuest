import ast
from functools import reduce

from engine.inputs import Case, random_int


def _params(T):
    return {a.arg for f in ast.walk(T.tree())
            if isinstance(f, ast.FunctionDef) for a in f.args.args}


def cases():
    cs = [Case(args=([1, 2, 3, 4],), expect=24),
          Case(args=([5],), expect=5),
          Case(args=([],), expect=1)]
    for _ in range(8):
        nums = [random_int(-6, 6) for _ in range(random_int(1, 6))]
        cs.append(Case(args=(nums,),
                       expect=reduce(lambda a, b: a * b, nums, 1)))
    return cs


def check(T):
    for c in cases():
        T.eq(T.call("product", *c.args), c.expect,
             because="product(%r) -> %r" % (c.args[0], c.expect))
    T.uses_import("functools",
                  because="Fold with reduce from functools, not a manual "
                          "accumulator loop.")
    T.uses_call("reduce",
                because="The lesson is reduce -- use it to combine the numbers.")
    # reduce must fold the INPUT itself. A manual accumulator loop that computes
    # the product, then reduce(f, [result], 1) wrapping it, does not fold the
    # input: require a live reduce(func, nums, ...) whose iterable is the
    # parameter, so reduce over a one-element [result] no longer counts.
    params = _params(T)
    live = [i for i, n in enumerate(ast.walk(T.tree()))
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
            and n.func.id == "reduce" and len(n.args) >= 2
            and isinstance(n.args[1], ast.Name) and n.args[1].id in params]
    T.require_live("reduce(func, nums, start) folding the input itself",
                   "reduce must fold the input list, not a one-element list "
                   "holding a product a manual loop already computed",
                   live, "expr",
                   because="The lesson is reduce doing the fold.")
