from engine.inputs import random_int


def check(T):
    T.eq(T.run(stdin="5\n1\n2\n3\n4\n-6\n"), "2\n4\n-6",
         because="Evens only, original order; -6 is even.")
    T.eq(T.run(stdin="3\n1\n3\n5\n"), "",
         because="No evens at all -> nothing printed.")
    T.eq(T.run(stdin="1\n0\n"), "0",
         because="0 is even (0 % 2 == 0).")
    for _ in range(8):
        k = random_int(0, 8)
        nums = [random_int(-20, 20) for _ in range(k)]
        stdin = "%d\n" % k + "".join("%d\n" % x for x in nums)
        expect = "\n".join("%d" % x for x in nums if x % 2 == 0)
        T.eq(T.run(stdin=stdin), expect,
             because="The even items of %r, in order" % nums)
    T.uses_comprehension(with_if=True,
                         because="The lesson is the filtering form: "
                                 "[x for x in nums if x % 2 == 0].")
