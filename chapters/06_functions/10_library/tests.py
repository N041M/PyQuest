from engine.inputs import Case, random_word


def vowels(w):
    return sum(1 for ch in w if ch in "aeiou")


def check(T):
    T.eq(T.call("count_vowels", "tea"), 2)
    T.eq(T.call("count_vowels", "xyz"), 0,
         because="No vowels at all is a count of 0.")
    T.eq(T.call("count_vowels", ""), 0,
         because="An empty word has zero vowels.")
    for _ in range(6):
        w = random_word(1, 10)
        T.eq(T.call("count_vowels", w), vowels(w),
             because="The vowel count of %r." % w)

    T.eq(T.call("describe", "tea"), "tea has 2 vowels")
    T.eq(T.call("describe", "xyz"), "xyz has no vowels",
         because="A zero count gets the special 'no vowels' wording.")
    for _ in range(6):
        w = random_word(1, 10)
        n = vowels(w)
        expect = ("%s has no vowels" % w if n == 0
                  else "%s has %d vowels" % (w, n))
        T.eq(T.call("describe", w), expect,
             because="describe(%r)." % w)
    T.uses_call("count_vowels",
                because="describe should DELEGATE to count_vowels, not "
                        "recount the vowels itself.")
