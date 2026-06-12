from engine.inputs import random_int


def check(T):
    T.eq(T.run(stdin="10\n"), "even", because="10 is even.")
    T.eq(T.run(stdin="7\n"), "odd", because="7 is odd.")
    T.eq(T.run(stdin="0\n"), "even", because="0 is even.")
    for _ in range(8):
        n = random_int(-50, 50)
        T.eq(T.run(stdin="%d\n" % n), "even" if n % 2 == 0 else "odd",
             because="%d is %s." % (n, "even" if n % 2 == 0 else "odd"))
    T.uses_if(because="Use an if/else statement.")
