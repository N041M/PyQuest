import re

from engine.inputs import Case, random_word, random_int


def _candidate():
    letters = random_word(2, 2).upper()
    kind = random_int(0, 3)
    if kind == 0:                                   # valid: AA9999
        return letters + "%04d" % random_int(0, 9999)
    if kind == 1:                                   # lowercase letters
        return random_word(2, 2) + "%04d" % random_int(0, 9999)
    if kind == 2:                                   # too few digits
        return letters + "%03d" % random_int(0, 999)
    return letters + "%04d" % random_int(0, 9999) + "x"   # trailing junk


def cases():
    cs = [Case(args=("AB1234",), expect=True),
          Case(args=("ab1234",), expect=False),
          Case(args=("AB123",), expect=False),
          Case(args=("AB1234x",), expect=False)]
    for _ in range(8):
        text = _candidate()
        cs.append(Case(args=(text,),
                       expect=re.fullmatch(r"[A-Z]{2}\d{4}", text) is not None))
    return cs


def check(T):
    for c in cases():
        T.eq(T.call("is_valid_code", *c.args), c.expect,
             because="is_valid_code(%r) should be %r" % (c.args[0], c.expect))
    T.uses_import("re",
                  because="Validate the whole string with re.fullmatch (or "
                          "^...$), not a hand-written length/character check.")
