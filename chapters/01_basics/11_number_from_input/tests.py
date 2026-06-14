from engine.inputs import random_int


def check(T):
    # fixed edges
    T.eq(T.run(stdin="0\n"), "0", because="Edge case: zero doubled is 0.")
    T.eq(T.run(stdin="-5\n"), "-10",
         because="Edge case: negatives double too: -5 -> -10.")
    # randomized values so the answer can't be hardcoded
    for _ in range(6):
        n = random_int(-1000, 1000)
        T.eq(T.run(stdin="%d\n" % n), str(n * 2),
             because="Double %d is %d." % (n, n * 2))
    T.uses_call("int",
                because="The lesson is converting the text with int() before "
                        "the maths -- eval() and friends skip that idea.")
