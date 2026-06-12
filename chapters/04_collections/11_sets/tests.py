from engine.inputs import random_word, random_int


def check(T):
    T.eq(T.run(stdin="4\na\nb\na\nc\n"), "3",
         because="distinct of a, b, a, c is {a, b, c} -> 3")
    T.eq(T.run(stdin="0\n"), "0")
    for _ in range(8):
        k = random_int(0, 8)
        pool = [random_word(1, 3) for _ in range(3)]   # small pool -> duplicates
        words = [pool[random_int(0, len(pool) - 1)] for _ in range(k)]
        stdin = "%d\n" % k + "".join(w + "\n" for w in words)
        T.eq(T.run(stdin=stdin), str(len(set(words))),
             because="distinct count of %r" % words)
    T.uses_set(because="Use a set -- set(words) -- to drop duplicates.")
