import re

from engine.inputs import Case, random_word, random_int


def _make_text():
    parts = []
    for _ in range(random_int(1, 4)):
        parts.append(random_word(1, 4))
        if random_int(0, 1):
            parts.append(str(random_int(0, 99999)))
    return "-".join(parts)


def cases():
    cs = [Case(args=("call 555-1234",), expect="call #-#"),
          Case(args=("no digits",), expect="no digits")]
    for _ in range(8):
        text = _make_text()
        cs.append(Case(args=(text,), expect=re.sub(r"\d+", "#", text)))
    return cs


def check(T):
    for c in cases():
        T.eq(T.call("redact", *c.args), c.expect,
             because="redact(%r) -> %r" % (c.args[0], c.expect))
    T.uses_import("re",
                  because="Collapse each digit run with re.sub(r'\\d+', '#', ...), "
                          "not a character-by-character loop.")
