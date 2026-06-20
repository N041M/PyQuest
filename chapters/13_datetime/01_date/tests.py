from datetime import date

from engine.inputs import Case, random_int


def cases():
    cs = [Case(args=(2026, 6, 20), expect="2026-06-20"),
          Case(args=(1999, 1, 5), expect="1999-01-05")]
    for _ in range(8):
        y, m, d = random_int(1000, 2999), random_int(1, 12), random_int(1, 28)
        cs.append(Case(args=(y, m, d), expect=date(y, m, d).isoformat()))
    return cs


def check(T):
    for c in cases():
        T.eq(T.call("iso", *c.args), c.expect,
             because="iso%r -> %r" % (c.args, c.expect))
    T.uses_import("datetime",
                  because="Build a date object and call .isoformat(), not a "
                          "hand-formatted string.")
