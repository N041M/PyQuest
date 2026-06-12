from engine.inputs import random_int


def check(T):
    T.eq(T.run(stdin="3\n3\n1\n4\n"), "8")
    T.eq(T.run(stdin="0\n"), "0",
         because="sum of no numbers is 0.")
    T.eq(T.run(stdin="2\n-5\n3\n"), "-2",
         because="Negative numbers count too.")
    for _ in range(8):
        k = random_int(0, 8)
        nums = [random_int(-20, 20) for _ in range(k)]
        stdin = "%d\n" % k + "".join("%d\n" % x for x in nums)
        T.eq(T.run(stdin=stdin), "%d" % sum(nums),
             because="sum of %r" % nums)
    T.uses_call("sum", because="The lesson is the built-in sum() -- "
                               "let it replace the accumulator loop.")
