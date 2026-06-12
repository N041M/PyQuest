from engine.inputs import random_int


def expected(pairs):
    return "\n".join([str(pairs)] + [str(a + b) for a, b in pairs])


def check(T):
    T.eq(T.run(stdin="2\n1\n2\n3\n4\n"), "[[1, 2], [3, 4]]\n3\n7")
    T.eq(T.run(stdin="0\n"), "[]", because="No pairs -> empty nested list.")
    for _ in range(8):
        k = random_int(0, 4)
        pairs = [[random_int(-9, 9), random_int(-9, 9)] for _ in range(k)]
        stdin = "%d\n" % k + "".join("%d\n%d\n" % (a, b) for a, b in pairs)
        T.eq(T.run(stdin=stdin), expected(pairs),
             because="nested list %r then each pair's sum" % pairs)
    T.uses_for(because="Loop over the nested list to sum each pair.")
