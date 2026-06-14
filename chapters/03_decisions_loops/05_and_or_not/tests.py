from engine.inputs import random_int


def check(T):
    T.eq(T.run(stdin="12\n"), "True", because="12 is divisible by 2 and 3.")
    T.eq(T.run(stdin="4\n"), "False", because="4 is not divisible by 3.")
    T.eq(T.run(stdin="9\n"), "False", because="9 is not divisible by 2.")
    T.eq(T.run(stdin="0\n"), "True", because="0 is divisible by both.")
    for _ in range(8):
        n = random_int(-30, 30)
        expect = (n % 2 == 0) and (n % 3 == 0)
        T.eq(T.run(stdin="%d\n" % n), str(expect),
             because="%d divisible by both 2 and 3 -> %s." % (n, expect))
    T.uses_boolop(
        because="The lesson is COMBINING two checks with a boolean operator "
                "(n % 2 == 0 and n % 3 == 0). Collapsing it to one modulo "
                "(n % 6 == 0) gets the right answer but skips the concept.")
