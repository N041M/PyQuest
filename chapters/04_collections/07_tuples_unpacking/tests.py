from engine.inputs import random_int


def check(T):
    T.eq(T.run(stdin="3\n7\n"), "7\n3")
    T.eq(T.run(stdin="5\n5\n"), "5\n5",
         because="Swapping two equal values looks the same.")
    for _ in range(8):
        a, b = random_int(-50, 50), random_int(-50, 50)
        T.eq(T.run(stdin="%d\n%d\n" % (a, b)), "%d\n%d" % (b, a),
             because="swap %d, %d -> %d, %d" % (a, b, b, a))
    T.uses_unpacking(
        because="Swap with tuple unpacking (a, b = b, a), not by printing in "
                "reverse order.")
