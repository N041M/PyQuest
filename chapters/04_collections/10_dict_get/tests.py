from engine.inputs import random_word, random_int


def check(T):
    T.eq(T.run(stdin="2\na\n1\nb\n2\nc\n"), "0",
         because="'c' is not a key, so the default 0 is printed.")
    T.eq(T.run(stdin="2\na\n1\nb\n2\na\n"), "1")
    for _ in range(8):
        k = random_int(0, 5)
        keys = []
        while len(keys) < k:
            w = random_word(2, 6)
            if w not in keys:
                keys.append(w)
        vals = {key: random_int(1, 99) for key in keys}   # values >= 1
        if keys and random_int(0, 1):
            query = keys[random_int(0, len(keys) - 1)]
            expect = vals[query]
        else:
            query = random_word(7, 9)
            while query in keys:
                query = random_word(7, 9)
            expect = 0
        stdin = "%d\n" % k + "".join("%s\n%d\n" % (key, vals[key])
                                     for key in keys) + query + "\n"
        T.eq(T.run(stdin=stdin), str(expect),
             because="get(%r, 0) = %d" % (query, expect))
    T.uses_call("get", because="Use d.get(key, 0) for a safe default.")
