from engine.inputs import random_word


def check(T):
    # edge: a one-letter word is its own first character
    T.eq(T.run(stdin="Q\n"), "Q",
         because="A one-letter word: its first character is itself.")
    # randomized so the answer cannot be hardcoded
    for _ in range(8):
        w = random_word(1, 10)
        T.eq(T.run(stdin=w + "\n"), w[0],
             because="The first character of %r is %r." % (w, w[0]))
    T.uses_index(because="Use indexing -- s[0] -- to get the first character.")
