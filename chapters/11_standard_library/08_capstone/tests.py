import json
import statistics

from engine.inputs import Case, random_int


def _expected(nums):
    return {"count": len(nums), "mean": statistics.mean(nums),
            "max": max(nums), "min": min(nums)}


def cases():
    cs = [Case(args=("[2, 4, 6]",), expect=_expected([2, 4, 6])),
          Case(args=("[5]",), expect=_expected([5]))]
    for _ in range(8):
        nums = [random_int(-50, 50) for _ in range(random_int(1, 7))]
        cs.append(Case(args=(json.dumps(nums),), expect=_expected(nums)))
    return cs


def check(T):
    for c in cases():
        T.approx(T.call("summary", *c.args), c.expect,
                 because="summary(%r) -> %r" % (c.args[0], c.expect))
    T.uses_import("json",
                  because="Parse the input with json.loads -- the capstone is "
                          "composing the library tools, not hand-parsing.")
