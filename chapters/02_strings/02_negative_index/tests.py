from engine.inputs import random_word


def check(T):
    T.eq(T.run(stdin="Q\n"), "Q",
         because="In a one-letter word, -1 points at that single character.")
    for _ in range(8):
        w = random_word(1, 10)
        T.eq(T.run(stdin=w + "\n"), w[-1],
             because="The last character of %r is %r." % (w, w[-1]))
    T.uses_negative_index(
        because="Use a negative index -- s[-1] -- not s[len(s)-1].")
