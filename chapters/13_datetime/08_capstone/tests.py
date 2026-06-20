from datetime import date, datetime, timedelta

from engine.inputs import Case, random_int


def cases():
    cs = [Case(args=("2026-06-20 23:30", 2), expect="2026-06-21 01:30"),
          Case(args=("2026-01-01 00:30", -1), expect="2025-12-31 23:30")]
    for _ in range(8):
        d = date(random_int(1100, 2900), random_int(1, 12), random_int(1, 28))
        hh, mm = random_int(0, 23), random_int(0, 59)
        text = "%s %02d:%02d" % (d.isoformat(), hh, mm)
        hours = random_int(-100, 100)
        dt = datetime.strptime(text, "%Y-%m-%d %H:%M") + timedelta(hours=hours)
        cs.append(Case(args=(text, hours), expect=dt.strftime("%Y-%m-%d %H:%M")))
    return cs


def check(T):
    for c in cases():
        T.eq(T.call("add_hours", *c.args), c.expect,
             because="add_hours(%r, %r) -> %r" % (c.args + (c.expect,)))
    T.uses_import("datetime",
                  because="Parse, shift with timedelta, and format back -- the "
                          "rollover is the library's job, not hand arithmetic.")
