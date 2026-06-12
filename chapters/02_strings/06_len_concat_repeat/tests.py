from engine.inputs import random_word


def expected(w):
    return "%d\n%s!\n%s" % (len(w), w, w * 3)


def check(T):
    T.eq(T.run(stdin="\n"), "0\n!",
         because="Empty input: length 0, just '!', and an empty repeat.")
    for _ in range(8):
        w = random_word(1, 10)
        T.eq(T.run(stdin=w + "\n"), expected(w),
             because="For %r: length, then %r, then it three times."
                     % (w, w + "!"))
    # (no construct check: s*3 and s+s+s are comparable for three repeats, and
    #  the brief doesn't frame one as the "wrong" way -- accept both.)
