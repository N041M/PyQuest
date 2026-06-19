from engine.inputs import random_word, random_int


def check(T):
    # case IS the lesson here, so these comparisons are case-sensitive.
    T.eq(T.run(stdin="a b\n"), "A B", match_case=True,
         because="Inner spaces stay; only the ends are stripped, and it's"
                 " UPPERCASE.")
    T.eq(T.run(stdin="   \n"), "", match_case=True,
         because="A line of only spaces becomes empty after stripping.")
    for _ in range(8):
        w = random_word(1, 10)
        padded = " " * random_int(0, 4) + w + " " * random_int(0, 4)
        T.eq(T.run(stdin=padded + "\n"), w.upper(), match_case=True,
             because="Stripped and uppercased, %r becomes %r."
                     % (padded, w.upper()))
    # The lesson IS the string methods: pin them so a hand-rolled trim/upcase
    # (slice off spaces, ord-math the case) can't pass without them. Liveness
    # keeps these honest -- both methods change the recorded output.
    T.uses_call("strip", because="Trim the ends with .strip(), not by hand.")
    T.uses_call("upper", because="Upper-case with .upper(), not ord() math.")
