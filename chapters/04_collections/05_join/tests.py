from engine.inputs import random_word, random_int


def check(T):
    T.eq(T.run(stdin="3\na\nb\nc\n"), "a-b-c")
    T.eq(T.run(stdin="1\nhello\n"), "hello")
    T.eq(T.run(stdin="0\n"), "", because="Nothing to join -> empty line.")
    for _ in range(8):
        k = random_int(0, 6)
        words = [random_word(1, 6) for _ in range(k)]
        stdin = "%d\n" % k + "".join(w + "\n" for w in words)
        T.eq(T.run(stdin=stdin), "-".join(words),
             because="%r joined with '-' is %r." % (words, "-".join(words)))
    T.uses_call("join", because='Use "-".join(words) to glue them together.')
