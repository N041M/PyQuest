from engine.inputs import random_word, random_int


def check(T):
    T.eq(T.run(stdin="3\ntea\nmilk\nsugar\n"),
         "1. tea\n2. milk\n3. sugar",
         because="Numbered from 1, in the format `1. word`.")
    T.eq(T.run(stdin="0\n"), "",
         because="No words, no output.")
    for _ in range(8):
        k = random_int(0, 6)
        words = [random_word(2, 8) for _ in range(k)]
        stdin = "%d\n" % k + "".join(w + "\n" for w in words)
        expect = "\n".join("%d. %s" % (i + 1, w) for i, w in enumerate(words))
        T.eq(T.run(stdin=stdin), expect,
             because="A 1-based numbered list of %r" % (words,))
    T.uses_call("enumerate", because="The lesson is enumerate() -- it tracks "
                                     "the position for you.")
