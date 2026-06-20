import statistics

from engine.inputs import Case, random_int


def cases():
    cs = [Case(args=([2, 4, 6],), expect=4),
          Case(args=([1, 2],), expect=1.5),
          Case(args=([5],), expect=5)]
    for _ in range(8):
        nums = [random_int(-20, 20) for _ in range(random_int(1, 6))]
        cs.append(Case(args=(nums,), expect=statistics.mean(nums)))
    return cs


def check(T):
    for c in cases():
        T.approx(T.call("average", *c.args), c.expect,
                 because="average(%r) is the mean, %r" % (c.args[0], c.expect))
    T.uses_import("statistics",
                  because="Take the mean from the statistics module (imported as "
                          "stats), not sum(nums) / len(nums) by hand.")
