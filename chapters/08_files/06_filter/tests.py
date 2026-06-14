from engine.inputs import random_word, random_int


def expected(raw):
    return "".join(s + "\n" for s in raw if s.strip())


def check(T):
    raw = ["keep me", "", "and me"]
    T.run(files={"lines.txt": "".join(s + "\n" for s in raw)})
    T.eq(T.file("kept.txt"), expected(raw),
         because="Blank lines dropped, the rest kept in order.")

    raw = ["alpha", "beta", "gamma"]
    T.run(files={"lines.txt": "".join(s + "\n" for s in raw)})
    T.eq(T.file("kept.txt"), expected(raw),
         because="No blank lines means an unchanged copy.")

    raw = ["", "   ", ""]
    T.run(files={"lines.txt": "".join(s + "\n" for s in raw)})
    T.eq(T.file("kept.txt"), "",
         because="An all-blank file produces an empty kept.txt.")

    for _ in range(8):
        raw = []
        for _ in range(random_int(2, 8)):
            raw.append("" if random_int(0, 1) else random_word(2, 8))
        T.run(files={"lines.txt": "".join(s + "\n" for s in raw)})
        T.eq(T.file("kept.txt"), expected(raw),
             because="Exactly the non-blank lines of %r." % raw)
    T.uses_with_open(because="Open both files with `with open(...) as f:`.")
