from engine.inputs import random_int


def check(T):
    T.eq(T.run(stdin="4\n"), "0\n1\n2\n3")
    T.eq(T.run(stdin="1\n"), "0")
    T.eq(T.run(stdin="0\n"), "", because="range(0) is empty.")
    for _ in range(6):
        n = random_int(1, 12)
        expect = "\n".join(str(i) for i in range(n))
        T.eq(T.run(stdin="%d\n" % n), expect,
             because="range(%d) prints 0..%d." % (n, n - 1))
    T.uses_for(because="This puzzle is about for + range -- use a for loop.")
