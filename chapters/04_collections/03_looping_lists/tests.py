from engine.inputs import random_int


def expected(nums):
    return "\n".join([str(len(nums))] + [str(x * 2) for x in nums])


def check(T):
    T.eq(T.run(stdin="3\n5\n2\n9\n"), "3\n10\n4\n18")
    T.eq(T.run(stdin="0\n"), "0", because="No numbers: just the count 0.")
    for _ in range(8):
        k = random_int(0, 6)
        nums = [random_int(-15, 15) for _ in range(k)]
        stdin = "%d\n" % k + "".join("%d\n" % x for x in nums)
        T.eq(T.run(stdin=stdin), expected(nums),
             because="Count then each doubled, for %r." % nums)
    T.uses_for(because="Loop over the list with a for loop.")
