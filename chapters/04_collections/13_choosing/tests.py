from engine.inputs import random_int


def check(T):
    T.eq(T.run(stdin="4\n1\n2\n2\n3\n"), "4\n3\n8")
    T.eq(T.run(stdin="0\n"), "0\n0\n0")
    for _ in range(8):
        k = random_int(0, 8)
        nums = [random_int(0, 5) for _ in range(k)]    # small range -> repeats
        stdin = "%d\n" % k + "".join("%d\n" % x for x in nums)
        expect = "%d\n%d\n%d" % (len(nums), len(set(nums)), sum(nums))
        T.eq(T.run(stdin=stdin), expect,
             because="count/distinct/sum of %r" % nums)
    T.uses_set(because="Use a set for the distinct count.")
