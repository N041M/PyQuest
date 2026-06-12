from engine.inputs import random_int


def check(T):
    T.eq(T.run(stdin="-4\n"), "negative", because="-4 is negative.")
    T.eq(T.run(stdin="7\n"), "", because="7 is not negative -> no output.")
    T.eq(T.run(stdin="0\n"), "", because="0 is not negative -> no output.")
    for _ in range(8):
        n = random_int(-50, 50)
        T.eq(T.run(stdin="%d\n" % n), "negative" if n < 0 else "",
             because="%d %s negative." % (n, "is" if n < 0 else "is not"))
    T.uses_if(because="Use an if statement -- not a trick that avoids it.")
