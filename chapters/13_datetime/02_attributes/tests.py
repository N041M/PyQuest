from datetime import date

from engine.inputs import Case, random_int


def cases():
    cs = [Case(args=("2026-06-20",), expect=(2026, 6, 20)),
          Case(args=("1999-01-05",), expect=(1999, 1, 5))]
    for _ in range(8):
        y, m, d = random_int(1000, 2999), random_int(1, 12), random_int(1, 28)
        text = date(y, m, d).isoformat()
        cs.append(Case(args=(text,), expect=(y, m, d)))
    return cs


def check(T):
    for c in cases():
        T.eq(T.call("parts", *c.args), c.expect,
             because="parts(%r) -> %r" % (c.args[0], c.expect))
    T.uses_import("datetime",
                  because="Parse with date.fromisoformat and read its attributes, "
                          "not text.split('-').")
