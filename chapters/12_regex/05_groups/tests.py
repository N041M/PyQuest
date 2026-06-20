from engine.inputs import Case, random_int


def cases():
    cs = [Case(args=("2026-06-20",), expect=(2026, 6, 20)),
          Case(args=("1999-01-05",), expect=(1999, 1, 5))]
    for _ in range(8):
        y, mo, d = random_int(1900, 2100), random_int(1, 12), random_int(1, 28)
        text = "%04d-%02d-%02d" % (y, mo, d)
        cs.append(Case(args=(text,), expect=(y, mo, d)))
    return cs


def check(T):
    for c in cases():
        T.eq(T.call("parse_date", *c.args), c.expect,
             because="parse_date(%r) -> %r" % (c.args[0], c.expect))
    T.uses_import("re",
                  because="Pull the fields out with capture groups via re.match, "
                          "not text.split('-').")
