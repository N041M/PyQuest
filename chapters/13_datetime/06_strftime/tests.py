from datetime import date

from engine.inputs import Case, random_int


def cases():
    cs = [Case(args=("2026-06-20",), expect="20/06/2026"),
          Case(args=("1999-01-05",), expect="05/01/1999")]
    for _ in range(8):
        d = date(random_int(1000, 2999), random_int(1, 12), random_int(1, 28))
        cs.append(Case(args=(d.isoformat(),), expect=d.strftime("%d/%m/%Y")))
    return cs


def check(T):
    for c in cases():
        T.eq(T.call("pretty", *c.args), c.expect,
             because="pretty(%r) -> %r" % (c.args[0], c.expect))
    T.uses_import("datetime",
                  because="Render with strftime('%d/%m/%Y') on a date, not by "
                          "rearranging split pieces of the string.")
