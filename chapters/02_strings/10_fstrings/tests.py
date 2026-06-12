from engine.inputs import random_word


def check(T):
    T.eq(T.run(stdin="a\n"), "a reversed is a",
         because="A single letter reversed is itself.")
    for _ in range(8):
        w = random_word(2, 10)
        T.eq(T.run(stdin=w + "\n"), "%s reversed is %s" % (w, w[::-1]),
             because="For %r the sentence is %r."
                     % (w, "%s reversed is %s" % (w, w[::-1])))
    T.uses_fstring(because="Build it with an f-string, not + concatenation.")
