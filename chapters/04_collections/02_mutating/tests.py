from engine.inputs import random_int


def expected(nums):
    nums = list(nums)
    nums[0] = nums[0] * 2
    nums.pop()
    return str(nums)


def check(T):
    T.eq(T.run(stdin="3\n5\n2\n9\n"), "[10, 2]")
    T.eq(T.run(stdin="1\n4\n"), "[]",
         because="Double 4 -> [8], then pop the only item -> [].")
    for _ in range(8):
        k = random_int(1, 6)
        nums = [random_int(-15, 15) for _ in range(k)]
        stdin = "%d\n" % k + "".join("%d\n" % x for x in nums)
        T.eq(T.run(stdin=stdin), expected(nums),
             because="From %r: double first, pop last -> %s"
                     % (nums, expected(nums)))
    T.uses_call("pop", because="Remove the last item with .pop() (mutate it).")
