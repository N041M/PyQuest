from engine.inputs import random_int


def check(T):
    T.eq(T.run(stdin="3\n10\n20\n5\n"), "35")
    T.eq(T.run(stdin="0\n"), "0", because="Count 0 -> sum 0, no numbers read.")
    T.eq(T.run(stdin="1\n-5\n"), "-5", because="Negatives are fine.")
    for _ in range(8):
        k = random_int(0, 6)
        nums = [random_int(-30, 30) for _ in range(k)]
        stdin = "%d\n" % k + "".join("%d\n" % n for n in nums)
        T.eq(T.run(stdin=stdin), str(sum(nums)),
             because="Sum of %r is %d." % (nums, sum(nums)))
    T.uses_loop(because="Build the total in a loop -- not with sum(...).")
