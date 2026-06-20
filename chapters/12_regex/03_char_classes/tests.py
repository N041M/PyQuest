import re

from engine.inputs import Case, random_word, random_int


def cases():
    cs = [Case(args=("education",), expect=5),
          Case(args=("xyz",), expect=0),
          Case(args=("",), expect=0)]
    for _ in range(8):
        text = "".join(random_word(2, 6) for _ in range(random_int(1, 3)))
        cs.append(Case(args=(text,), expect=len(re.findall(r"[aeiou]", text))))
    return cs


def check(T):
    for c in cases():
        T.eq(T.call("count_vowels", *c.args), c.expect,
             because="count_vowels(%r) -> %r" % (c.args[0], c.expect))
    T.uses_import("re",
                  because="Match vowels with a [aeiou] class via re.findall, not "
                          "a manual 'c in \"aeiou\"' loop.")
