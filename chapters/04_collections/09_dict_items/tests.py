from engine.inputs import random_word, random_int


def check(T):
    T.eq(T.run(stdin="2\na\n1\nb\n2\n"), "a=1\nb=2")
    T.eq(T.run(stdin="0\n"), "", because="Empty dict -> no lines.")
    for _ in range(8):
        k = random_int(0, 5)
        keys = []
        while len(keys) < k:
            w = random_word(2, 6)
            if w not in keys:
                keys.append(w)
        vals = {key: random_int(0, 99) for key in keys}
        stdin = "%d\n" % k + "".join("%s\n%d\n" % (key, vals[key])
                                     for key in keys)
        expect = "\n".join("%s=%d" % (key, vals[key]) for key in keys)
        T.eq(T.run(stdin=stdin), expect,
             because="key=value lines for %r" % vals)
    T.uses_call("items", because="Loop with for k, v in d.items().")
