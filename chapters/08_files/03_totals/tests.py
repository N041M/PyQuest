from engine.inputs import random_int


def check(T):
    T.eq(T.run(files={"prices.txt": "10\n25\n7\n"}), "42",
         because="Sum of every number in the file.")
    T.eq(T.run(files={"prices.txt": "5\n"}), "5",
         because="A single line totals to itself.")
    T.eq(T.run(files={"prices.txt": "10\n-4\n-6\n"}), "0",
         because="Negative numbers count too.")
    for _ in range(8):
        nums = [random_int(-50, 50) for _ in range(random_int(1, 8))]
        text = "".join("%d\n" % n for n in nums)
        T.eq(T.run(files={"prices.txt": text}), "%d" % sum(nums),
             because="The total of %r is %d." % (nums, sum(nums)))
    T.uses_with_open(because="Open the file with `with open(...) as f:`.")
    T.uses_call("int",
                because="File lines are text -- convert each with int() before "
                        "adding, or you'd be concatenating strings.")
