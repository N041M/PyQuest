from engine.inputs import random_word, random_int


def sprinkle(w):
    """Drop a few 'o's into a word so replace/count have work to do."""
    chars = list(w)
    for _ in range(random_int(0, 3)):
        chars.insert(random_int(0, len(chars)), "o")
    return "".join(chars)


def expected(s):
    return "%s\n%d" % (s.replace("o", "0"), s.count("o"))


def check(T):
    T.eq(T.run(stdin="xyz\n"), "xyz\n0",
         because="No 'o': the line is unchanged and the count is 0.")
    T.eq(T.run(stdin="foobar\n"), "f00bar\n2")
    for _ in range(8):
        s = sprinkle(random_word(2, 8))
        T.eq(T.run(stdin=s + "\n"), expected(s),
             because="For %r: replace every o with 0, then count the o's." % s)
    T.uses_call("replace",
                because="The lesson is s.replace('o', '0') -- let the method "
                        "swap them, don't rebuild the string by hand.")
    T.uses_call("count",
                because="The lesson is s.count('o') -- let it tally the o's, "
                        "not a hand-written loop.")
