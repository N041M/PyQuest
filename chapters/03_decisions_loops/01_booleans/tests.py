from engine.inputs import random_int


def check(T):
    T.eq(T.run(stdin="8\n3\n"), "True",
         because="8 > 3 is True.")
    T.eq(T.run(stdin="2\n5\n"), "False",
         because="2 > 5 is False.")
    T.eq(T.run(stdin="4\n4\n"), "False",
         because="Equal is not 'greater', so 4 > 4 is False.")
    for _ in range(8):
        a, b = random_int(-50, 50), random_int(-50, 50)
        T.eq(T.run(stdin="%d\n%d\n" % (a, b)), str(a > b),
             because="%d > %d is %s." % (a, b, a > b))
