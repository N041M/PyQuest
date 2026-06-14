from engine.inputs import random_int


def label(n):
    if n > 0:
        return "small" if n < 100 else "big"
    return "non-positive"


def check(T):
    T.eq(T.run(stdin="-1\n"), "non-positive")
    T.eq(T.run(stdin="0\n"), "non-positive", because="0 is not positive.")
    T.eq(T.run(stdin="42\n"), "small")
    T.eq(T.run(stdin="100\n"), "big", because="100 is the 'big' boundary.")
    T.eq(T.run(stdin="500\n"), "big")
    for _ in range(8):
        n = random_int(-50, 300)
        T.eq(T.run(stdin="%d\n" % n), label(n),
             because="%d -> %s." % (n, label(n)))
    T.uses_nested_if(
        because="The lesson is a NESTED if: an outer check for positive, the "
                "size check inside it. A flat if/elif chain gets the same "
                "answer but skips the nesting.")
