from engine.inputs import random_int


def check(T):
    T.eq(T.run(stdin="3\n"), "1\n2\n3")
    T.eq(T.run(stdin="1\n"), "1")
    T.eq(T.run(stdin="0\n"), "", because="The loop body never runs for 0.")
    T.eq(T.run(stdin="-4\n"), "", because="Negative counts print nothing.")
    for _ in range(6):
        n = random_int(1, 12)
        expect = "\n".join(str(i) for i in range(1, n + 1))
        T.eq(T.run(stdin="%d\n" % n), expect,
             because="Counting 1..%d." % n)
    T.uses_while(because="This puzzle is about while -- use a while loop.")
