from engine.inputs import random_word


def check(T):
    # edges: 1- and 2-letter words have no middle
    T.eq(T.run(stdin="ab\n"), "",
         because="'ab' has no middle, so the slice is empty.")
    T.eq(T.run(stdin="a\n"), "",
         because="A single character has no middle either.")
    for _ in range(8):
        w = random_word(2, 12)
        T.eq(T.run(stdin=w + "\n"), w[1:-1],
             because="%r without its first and last character is %r."
                     % (w, w[1:-1]))
    T.uses_slice(because="Use a slice -- s[1:-1] -- not a loop.")
