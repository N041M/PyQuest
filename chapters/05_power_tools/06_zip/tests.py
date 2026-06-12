from engine.inputs import random_word, random_int


def check(T):
    T.eq(T.run(stdin="2\namy\nben\n90\n85\n"), "amy 90\nben 85",
         because="Names first, then scores -- paired in order.")
    T.eq(T.run(stdin="0\n"), "",
         because="No pairs, no output.")
    for _ in range(8):
        k = random_int(0, 6)
        names = [random_word(2, 7) for _ in range(k)]
        scores = [random_int(0, 100) for _ in range(k)]
        stdin = ("%d\n" % k + "".join(w + "\n" for w in names)
                 + "".join("%d\n" % s for s in scores))
        expect = "\n".join("%s %d" % (w, s) for w, s in zip(names, scores))
        T.eq(T.run(stdin=stdin), expect,
             because="Pairing %r with %r" % (names, scores))
    T.uses_call("zip", because="The lesson is zip() -- it walks both lists "
                               "in step.")
