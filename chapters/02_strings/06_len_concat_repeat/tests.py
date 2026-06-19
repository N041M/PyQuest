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
    # Pin len(): counting characters is the lesson, so a hand-rolled
    # sum(1 for _ in s) can't stand in for it. Repeat stays open on purpose --
    # s*3 and s+s+s are comparable, and the brief frames neither as wrong.
    T.uses_call("len", because="Count the characters with len(), not by hand.")
