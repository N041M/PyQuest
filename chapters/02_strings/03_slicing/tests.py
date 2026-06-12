from engine.inputs import random_word


def check(T):
    # edges: shorter than three, and empty
    T.eq(T.run(stdin="hi\n"), "hi",
         because="Slicing past the end is safe: 'hi'[:3] is just 'hi'.")
    T.eq(T.run(stdin="\n"), "",
         because="An empty input has no characters to take.")
    for _ in range(8):
        w = random_word(1, 12)
        T.eq(T.run(stdin=w + "\n"), w[:3],
             because="The first three characters of %r are %r." % (w, w[:3]))
    T.uses_slice(because="Use a slice -- s[:3] -- not a loop.")
