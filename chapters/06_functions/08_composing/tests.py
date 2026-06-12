from engine.inputs import Case, random_word, random_int


def messy(w):
    pad = " " * random_int(0, 3)
    mixed = "".join(c.upper() if random_int(0, 1) else c for c in w)
    return pad + mixed + " " * random_int(0, 3)


def check(T):
    T.eq(T.call("clean", "  Tea "), "tea", match_case=True,
         because="clean strips the ends and lowercases.")
    T.eq(T.call("clean", "ok"), "ok", match_case=True,
         because="Already-clean text passes through unchanged.")
    for _ in range(6):
        w = random_word(2, 8)
        m = messy(w)
        T.eq(T.call("clean", m), w, match_case=True,
             because="clean should reduce %r to %r." % (m, w))

    same = T.call("same_word", "  Tea ", "tea")
    T.is_a(same, bool, because="A comparison returns True or False -- "
                               "return it directly.")
    T.true(same is True, because="'  Tea ' and 'tea' match after cleaning.")
    T.true(T.call("same_word", "tea", "milk") is False,
           because="Different words stay different.")
    for _ in range(6):
        a = random_word(2, 7)
        b = a if random_int(0, 1) else random_word(2, 7)   # equal pairs too
        T.eq(T.call("same_word", messy(a), messy(b)), a == b,
             because="same_word(%r, %r) -- equal after cleaning?" % (a, b))
    T.uses_call("clean", because="same_word should DELEGATE to clean, not "
                                 "repeat the strip/lower recipe.")
