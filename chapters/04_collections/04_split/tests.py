from engine.inputs import random_word, random_int


def check(T):
    T.eq(T.run(stdin="the quick brown fox\n"), "4")
    T.eq(T.run(stdin="hello\n"), "1")
    T.eq(T.run(stdin="\n"), "0", because="An empty line has no words.")
    for _ in range(8):
        words = [random_word(1, 6) for _ in range(random_int(0, 7))]
        line = " ".join(words)
        T.eq(T.run(stdin=line + "\n"), str(len(words)),
             because="%r has %d words." % (line, len(words)))
    T.uses_call("split", because="Use .split() to break the line into words.")
