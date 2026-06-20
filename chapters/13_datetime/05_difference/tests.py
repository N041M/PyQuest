from datetime import date

from engine.inputs import Case, random_int


def cases():
    cs = [Case(args=("2026-06-20", "2026-07-01"), expect=11),
          Case(args=("2026-07-01", "2026-06-20"), expect=-11),
          Case(args=("2026-06-20", "2026-06-20"), expect=0)]
    for _ in range(8):
        da = date(random_int(1100, 2900), random_int(1, 12), random_int(1, 28))
        db = date(random_int(1100, 2900), random_int(1, 12), random_int(1, 28))
        cs.append(Case(args=(da.isoformat(), db.isoformat()),
                       expect=(db - da).days))
    return cs


def check(T):
    for c in cases():
        T.eq(T.call("days_between", *c.args), c.expect,
             because="days_between(%r, %r) -> %r" % (c.args + (c.expect,)))
    T.uses_import("datetime",
                  because="Subtract the two date objects and read .days, not a "
                          "hand-written day count.")
