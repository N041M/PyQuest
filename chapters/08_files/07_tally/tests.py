from engine.inputs import random_word, random_int


def expected(words):
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    order = sorted(counts, key=lambda w: (-counts[w], w))
    return "".join("%s: %d\n" % (w, counts[w]) for w in order)


def run_with(T, words):
    text = "".join(w + "\n" for w in words)
    T.run(files={"words.txt": text})
    return T.file("report.txt")


def check(T):
    words = ["fig", "fig", "pear", "fig", "pear"]
    T.eq(run_with(T, words), expected(words),
         because="Counts, ordered by frequency then alphabetically.")

    T.eq(run_with(T, ["solo"]), "solo: 1",
         because="A single word reports a count of 1.")

    # ties: same count -> alphabetical order
    T.eq(run_with(T, ["beta", "alpha"]), "alpha: 1\nbeta: 1",
         because="Equal counts are broken alphabetically.")

    pool = ["red", "green", "blue", "gold", "grey"]
    for _ in range(8):
        words = [pool[random_int(0, len(pool) - 1)]
                 for _ in range(random_int(1, 12))]
        T.eq(run_with(T, words), expected(words),
             because="Frequency report for %r." % words)
    T.uses_with_open(because="Open both files with `with open(...) as f:`.")
    T.uses_dict(because="Tally the words with a dict (the dict.get pattern).")
