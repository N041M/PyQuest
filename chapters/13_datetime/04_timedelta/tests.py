from datetime import date, timedelta

from engine.inputs import Case, random_int


def cases():
    cs = [Case(args=("2026-06-20", 40), expect="2026-07-30"),
          Case(args=("2026-01-01", -1), expect="2025-12-31")]
    for _ in range(8):
        y, m, d = random_int(1100, 2900), random_int(1, 12), random_int(1, 28)
        n = random_int(-1000, 1000)
        text = date(y, m, d).isoformat()
        expect = (date(y, m, d) + timedelta(days=n)).isoformat()
        cs.append(Case(args=(text, n), expect=expect))
    return cs


def check(T):
    for c in cases():
        T.eq(T.call("add_days", *c.args), c.expect,
             because="add_days(%r, %r) -> %r" % (c.args + (c.expect,)))
    T.uses_import("datetime",
                  because="Shift the date with timedelta -- it handles month and "
                          "year rollover the library way.")
