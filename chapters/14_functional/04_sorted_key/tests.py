import ast

from engine.inputs import Case, random_word, random_int


def cases():
    cs = [Case(args=(["pear", "fig", "kiwi"],), expect=["fig", "kiwi", "pear"]),
          Case(args=([],), expect=[])]
    for _ in range(8):
        words = [random_word(1, 6) for _ in range(random_int(2, 7))]
        cs.append(Case(args=(words,),
                       expect=sorted(words, key=lambda w: w[-1])))
    return cs


def check(T):
    for c in cases():
        T.eq(T.call("by_last", *c.args), c.expect,
             because="by_last(%r) -> %r" % (c.args[0], c.expect))
    T.uses_call("sorted",
                because="Order the words with sorted(...), not a hand-written "
                        "sort.")
    # The lambda must be the SORT KEY itself, not a decoy parked elsewhere to
    # satisfy a bare uses_lambda while a named key function does the work:
    # require a live sorted(...) whose key= keyword is a lambda.
    live = [i for i, n in enumerate(ast.walk(T.tree()))
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
            and n.func.id == "sorted"
            and any(k.arg == "key" and isinstance(k.value, ast.Lambda)
                    for k in n.keywords)]
    T.require_live("sorted(..., key=lambda ...)",
                   "the sort key must be an inline lambda, not a named function "
                   "with a decoy lambda elsewhere",
                   live, "expr",
                   because="Sort by an inline key=lambda, the lesson here.")
