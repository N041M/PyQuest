from functools import reduce

from engine.inputs import Case, random_int


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
    # reduce must fold the INPUT itself, not a one-element [result] holding a
    # product a manual accumulator loop already computed.
    T.uses_call_over_param("reduce",
                           because="The lesson is reduce folding the numbers "
                                   "-- use it over the input list.")
