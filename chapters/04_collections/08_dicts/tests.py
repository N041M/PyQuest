from engine.inputs import random_word, random_int


def check(T):
    T.eq(T.run(stdin="2\napple\n3\nbanana\n5\nbanana\n"), "5")
    for _ in range(8):
        k = random_int(1, 5)
        keys = []
        while len(keys) < k:
            w = random_word(2, 6)
            if w not in keys:
                keys.append(w)
        d = {key: random_int(0, 100) for key in keys}
        query = keys[random_int(0, k - 1)]
        stdin = "%d\n" % k + "".join("%s\n%d\n" % (key, d[key]) for key in keys) \
            + query + "\n"
        T.eq(T.run(stdin=stdin), str(d[query]),
             because="the value stored for %r is %d" % (query, d[query]))
    T.uses_dict(because="Store the pairs in a dict and look up by key.")
