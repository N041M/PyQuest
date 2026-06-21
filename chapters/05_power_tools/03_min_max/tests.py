from engine.inputs import random_int


def check(T):
    T.eq(T.run(stdin="3\n4\n-2\n9\n"), "-2\n9")
    T.eq(T.run(stdin="1\n5\n"), "5\n5",
         because="One number is both the smallest and the largest.")
    for _ in range(8):
        k = random_int(1, 8)
        nums = [random_int(-50, 50) for _ in range(k)]
        stdin = "%d\n" % k + "".join("%d\n" % x for x in nums)
        T.eq(T.run(stdin=stdin), "%d\n%d" % (min(nums), max(nums)),
             because="min then max of %r" % nums)
    T.uses_call_on_collection("min", because="Use the built-in min() over the "
                                             "numbers, not min([lo]) wrapping a "
                                             "hand-tracked value.")
    T.uses_call_on_collection("max", because="Use the built-in max() over the "
                                             "numbers, not max([hi]) wrapping a "
                                             "hand-tracked value.")
