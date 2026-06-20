import re

from engine.inputs import Case, random_word, random_int


def _make_text():
    seps = [" ", ", ", ". ", "! ", "-", " "]
    words = [random_word(1, 6) for _ in range(random_int(1, 5))]
    text = words[0]
    for w in words[1:]:
        text += seps[random_int(0, len(seps) - 1)] + w
    return text


def cases():
    cs = [Case(args=("Hello, world!",), expect=["Hello", "world"]),
          Case(args=("one-two three",), expect=["one", "two", "three"]),
          Case(args=("",), expect=[])]
    for _ in range(8):
        text = _make_text()
        cs.append(Case(args=(text,), expect=re.findall(r"[A-Za-z]+", text)))
    return cs


def check(T):
    for c in cases():
        T.eq(T.call("find_words", *c.args), c.expect,
             because="find_words(%r) -> %r" % (c.args[0], c.expect))
    T.uses_import("re",
                  because="Match each word with [A-Za-z]+ via re.findall, not a "
                          "hand-written letter-run scan.")
