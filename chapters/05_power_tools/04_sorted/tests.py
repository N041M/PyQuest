from engine.inputs import random_int


def check(T):
    T.eq(T.run(stdin="4\n3\n1\n3\n2\n"), "1\n2\n3\n3",
         because="Sorting keeps duplicates -- the two 3s both appear.")
    T.eq(T.run(stdin="0\n"), "",
         because="No numbers, no output.")
    T.eq(T.run(stdin="3\n-1\n-5\n0\n"), "-5\n-1\n0",
         because="Negative numbers sort below zero.")
    for _ in range(8):
        k = random_int(0, 8)
        nums = [random_int(-30, 30) for _ in range(k)]
        stdin = "%d\n" % k + "".join("%d\n" % x for x in nums)
        expect = "\n".join("%d" % x for x in sorted(nums))
        T.eq(T.run(stdin=stdin), expect,
             because="%r in ascending order" % nums)
    T.uses_call("sorted", because="The lesson is sorted() -- let it do the "
                                  "ordering.")
