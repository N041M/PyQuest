from engine.inputs import random_word


def check(T):
    T.eq(T.run(stdin="cat\n"), "c\na\nt")
    T.eq(T.run(stdin="a\n"), "a")
    T.eq(T.run(stdin="\n"), "", because="An empty word prints nothing.")
    for _ in range(8):
        w = random_word(1, 10)
        T.eq(T.run(stdin=w + "\n"), "\n".join(w),
             because="Each character of %r on its own line." % w)
    T.uses_for(because="Loop over the string with a for loop.")
