from engine.inputs import random_word, random_int

LETTERS = "abcdefghijklmnopqrstuvwxyz"


def check(T):
    T.eq(T.run(stdin="banana\nn\n"), "yes",
         because="'n' appears in 'banana'.")
    T.eq(T.run(stdin="banana\nz\n"), "no",
         because="'z' is nowhere in 'banana'.")
    T.eq(T.run(stdin="a\na\n"), "yes",
         because="A one-letter word that IS the letter.")
    for _ in range(8):
        w = random_word(1, 10)
        letter = LETTERS[random_int(0, 25)]
        expect = "yes" if letter in w else "no"
        T.eq(T.run(stdin="%s\n%s\n" % (w, letter)), expect,
             because="Is %r in %r?" % (letter, w))
    T.uses_in(because="The lesson is the `in` operator -- use it instead of "
                      ".find() or .count().")
