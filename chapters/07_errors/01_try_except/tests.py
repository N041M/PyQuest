from engine.inputs import random_word, random_int


def check(T):
    T.eq(T.run(stdin="7\n"), "14")
    T.eq(T.run(stdin="-3\n"), "-6",
         because="Negative numbers still convert.")
    T.eq(T.run(stdin="seven\n"), "not a number",
         because="Bad input is handled, not crashed on.")
    T.eq(T.run(stdin="12abc\n"), "not a number",
         because="int() rejects mixed text like '12abc'.")
    for _ in range(8):
        if random_int(0, 1):
            n = random_int(-99, 99)
            T.eq(T.run(stdin="%d\n" % n), "%d" % (n * 2),
                 because="%r is a number: print its double." % n)
        else:
            w = random_word(2, 8)
            T.eq(T.run(stdin=w + "\n"), "not a number",
                 because="%r is not a number." % w)
    T.uses_try(because="The lesson is try/except -- recover from the "
                       "ValueError instead of avoiding it.")
