from engine.inputs import random_int


def label(n):
    if n < 0:
        return "negative"
    elif n == 0:
        return "zero"
    return "positive"


def check(T):
    T.eq(T.run(stdin="-3\n"), "negative")
    T.eq(T.run(stdin="0\n"), "zero", because="0 is exactly zero.")
    T.eq(T.run(stdin="5\n"), "positive")
    for _ in range(8):
        n = random_int(-30, 30)
        T.eq(T.run(stdin="%d\n" % n), label(n),
             because="%d is %s." % (n, label(n)))
    T.uses_if(because="Use if / elif / else -- not a one-line trick.")
