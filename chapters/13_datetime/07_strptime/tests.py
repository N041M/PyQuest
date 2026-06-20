from datetime import date

from engine.inputs import Case, random_int


def cases():
    cs = [Case(args=("2026-06-20 14:30",), expect=14),
          Case(args=("1999-01-05 09:05",), expect=9)]
    for _ in range(8):
        d = date(random_int(1000, 2999), random_int(1, 12), random_int(1, 28))
        hh, mm = random_int(0, 23), random_int(0, 59)
        text = "%s %02d:%02d" % (d.isoformat(), hh, mm)
        cs.append(Case(args=(text,), expect=hh))
    return cs


def check(T):
    for c in cases():
        T.eq(T.call("hour_of", *c.args), c.expect,
             because="hour_of(%r) -> %r" % (c.args[0], c.expect))
    T.uses_import("datetime",
                  because="Parse with datetime.strptime and read .hour, not by "
                          "slicing the string.")
