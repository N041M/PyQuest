from engine.inputs import random_word, random_int


def expected(text):
    lines = text.splitlines()
    return "\n".join("%d. %s" % (i, w) for i, w in enumerate(lines, 1))


def check(T):
    f1 = "wash\ncook\nsleep\n"
    T.eq(T.run(files={"tasks.txt": f1}), expected(f1),
         because="Number each line from 1, newline stripped.")
    f2 = "only one\n"
    T.eq(T.run(files={"tasks.txt": f2}), expected(f2),
         because="A single line is just '1. only one'.")
    for _ in range(8):
        lines = [random_word(2, 8) for _ in range(random_int(1, 6))]
        text = "".join(w + "\n" for w in lines)
        T.eq(T.run(files={"tasks.txt": text}), expected(text),
             because="Each line numbered in order.")
    T.uses_with_open(because="Open the file with `with open(...) as f:`.")
    T.uses_for(because="Walk the lines with a for loop over the file.")
