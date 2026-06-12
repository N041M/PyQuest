from engine.inputs import random_word, random_int


def check(T):
    T.eq(T.run(stdin="tea milk tea\ntea\n"), "2")
    T.eq(T.run(stdin="tea milk tea\nmilk\n"), "1")
    T.eq(T.run(stdin="tea milk tea\ncocoa\n"), "0",
         because="A word that never appears counts 0 -- it must not crash.")
    for _ in range(8):
        vocab = [random_word(2, 5) for _ in range(3)]
        k = random_int(0, 10)
        words = [vocab[random_int(0, 2)] for _ in range(k)]
        query = vocab[random_int(0, 2)]
        stdin = " ".join(words) + "\n" + query + "\n"
        T.eq(T.run(stdin=stdin), "%d" % words.count(query),
             because="How often %r appears in %r" % (query, words))
    T.uses_dict(because="The lesson is the dict tally pattern -- "
                        "counts[w] = counts.get(w, 0) + 1.")
    T.uses_call("get", because="Use .get(key, 0) so new and missing words "
                               "start from 0 instead of crashing.")
