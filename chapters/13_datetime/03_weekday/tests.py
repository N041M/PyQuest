from datetime import date

from engine.inputs import Case, random_int


def cases():
    cs = [Case(args=("2026-06-20",), expect=5),
          Case(args=("2000-01-01",), expect=5),
          Case(args=("2026-06-22",), expect=0)]
    for _ in range(8):
        y, m, d = random_int(1000, 2999), random_int(1, 12), random_int(1, 28)
        text = date(y, m, d).isoformat()
        cs.append(Case(args=(text,), expect=date(y, m, d).weekday()))
    return cs


def check(T):
    for c in cases():
        T.eq(T.call("weekday", *c.args), c.expect,
             because="weekday(%r) -> %r (Monday=0)" % (c.args[0], c.expect))
    T.uses_import("datetime",
                  because="Let the date object compute the weekday -- the calendar "
                          "logic is exactly what the library is for.")
