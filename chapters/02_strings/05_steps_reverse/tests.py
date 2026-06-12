from engine.inputs import random_word


def check(T):
    T.eq(T.run(stdin="level\n"), "level",
         because="A palindrome reads the same reversed.")
    T.eq(T.run(stdin="a\n"), "a")
    for _ in range(8):
        w = random_word(2, 12)
        T.eq(T.run(stdin=w + "\n"), w[::-1],
             because="%r reversed is %r." % (w, w[::-1]))
    T.uses_slice(step=True,
                 because="Use the slice step -- s[::-1] -- not a manual loop.")
