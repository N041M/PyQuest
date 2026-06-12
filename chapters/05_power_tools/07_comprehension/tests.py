from engine.inputs import random_int


def check(T):
    T.eq(T.run(stdin="3\n4\n-1\n0\n"), "8\n-2\n0",
         because="Each number doubled, order kept.")
    T.eq(T.run(stdin="0\n"), "",
         because="No numbers, no output.")
    for _ in range(8):
        k = random_int(0, 8)
        nums = [random_int(-25, 25) for _ in range(k)]
        stdin = "%d\n" % k + "".join("%d\n" % x for x in nums)
        expect = "\n".join("%d" % (x * 2) for x in nums)
        T.eq(T.run(stdin=stdin), expect,
             because="%r with every item doubled" % nums)
    T.uses_comprehension(because="The lesson is the comprehension form: "
                                 "[x * 2 for x in nums].")
