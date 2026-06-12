from engine.inputs import random_word, random_int


def check(T):
    T.eq(T.run(stdin="2\na\nb\n2\nb\nc\n"), "1",
         because="only 'b' is in both groups")
    T.eq(T.run(stdin="0\n0\n"), "0", because="two empty groups share nothing")
    for _ in range(8):
        pool = [random_word(1, 3) for _ in range(4)]

        def group():
            return [pool[random_int(0, 3)] for _ in range(random_int(0, 4))]

        a, b = group(), group()
        stdin = ("%d\n" % len(a) + "".join(w + "\n" for w in a)
                 + "%d\n" % len(b) + "".join(w + "\n" for w in b))
        expect = len(set(a) & set(b))
        T.eq(T.run(stdin=stdin), str(expect),
             because="shared count of %r and %r is %d" % (a, b, expect))
    T.uses_set(because="Use sets to find the overlap.")
