from engine.inputs import random_word, random_int


def expected(line):
    try:
        return "%d" % int(line)
    except ValueError as e:
        return str(e)


def check(T):
    T.eq(T.run(stdin="7\n"), "7")
    T.eq(T.run(stdin="5x\n"), expected("5x"), match_case=True,
         because="Relay Python's own ValueError message, offender quoted.")
    for _ in range(8):
        line = ("%d" % random_int(-99, 99) if random_int(0, 1)
                else random_word(2, 7))
        T.eq(T.run(stdin=line + "\n"), expected(line), match_case=True,
             because="For input %r, print the number or Python's exact "
                     "message -- only printing `e` matches every time." % line)
    T.uses_try(because="Catch the ValueError to get at its message.")
