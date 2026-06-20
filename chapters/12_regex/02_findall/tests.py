import re

from engine.inputs import Case, random_word, random_int


def _make_text():
    parts = []
    for _ in range(random_int(1, 4)):
        parts.append(random_word(1, 4))
        if random_int(0, 1):
            parts.append(str(random_int(0, 9999)))
    return "".join(parts)


def cases():
    cs = [Case(args=("a12b3c456",), expect=["12", "3", "456"]),
          Case(args=("nothing",), expect=[])]
    for _ in range(8):
        text = _make_text()
        cs.append(Case(args=(text,), expect=re.findall(r"\d+", text)))
    return cs


def check(T):
    for c in cases():
        T.eq(T.call("all_numbers", *c.args), c.expect,
             because="all_numbers(%r) -> %r" % (c.args[0], c.expect))
    T.uses_import("re",
                  because="Extract the runs with re.findall(r'\\d+', ...), not a "
                          "hand-written loop.")
    T.uses_call("findall",
                because="The lesson is re.findall -- use it to collect the "
                        "matches.")
