from engine.inputs import random_word, random_int


def _report(words):
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return "\n".join("%s %d" % (w, counts[w]) for w in sorted(counts))


def check(T):
    T.eq(T.run(stdin="tea milk tea\n"), "milk 1\ntea 2",
         because="Distinct words with counts, alphabetical.")
    T.eq(T.run(stdin="hi hi hi\n"), "hi 3",
         because="One repeated word -> one line with its full count.")
    T.eq(T.run(stdin="\n"), "",
         because="An empty line has no words to report.")
    for _ in range(8):
        vocab = [random_word(2, 5) for _ in range(3)]
        k = random_int(0, 12)
        words = [vocab[random_int(0, 2)] for _ in range(k)]
        T.eq(T.run(stdin=" ".join(words) + "\n"), _report(words),
             because="The word report for %r" % (words,))
    T.uses_dict(because="Tally the words in a dict first.")
    T.uses_call("sorted", because="sorted(counts) puts the report in "
                                  "alphabetical order.")
