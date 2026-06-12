from engine.inputs import random_int


def check(T):
    T.eq(T.run(stdin="4\n5\n0\n"), "9")
    T.eq(T.run(stdin="0\n"), "0", because="No numbers before 0 -> total 0.")
    T.eq(T.run(stdin="5\n-5\n2\n0\n"), "2", because="Negatives count too.")
    for _ in range(6):
        nums = [random_int(-20, 20) for _ in range(random_int(0, 6))]
        nums = [n for n in nums if n != 0]          # keep 0 only as the sentinel
        stdin = "".join("%d\n" % n for n in nums) + "0\n"
        T.eq(T.run(stdin=stdin), str(sum(nums)),
             because="Sum of %r is %d." % (nums, sum(nums)))
    T.uses_while(because="Use a while loop that stops at the sentinel.")
