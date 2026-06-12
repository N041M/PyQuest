from engine.inputs import random_int


def check(T):
    T.eq(T.run(stdin="3\n1\n2\n3\n"), "[1, 2, 3]")
    T.eq(T.run(stdin="0\n"), "[]", because="No numbers -> an empty list.")
    for _ in range(8):
        k = random_int(0, 6)
        nums = [random_int(-20, 20) for _ in range(k)]
        stdin = "%d\n" % k + "".join("%d\n" % x for x in nums)
        T.eq(T.run(stdin=stdin), str(nums),
             because="The collected list should be %r." % nums)
    T.uses_call("append", because="Build the list with .append().")
