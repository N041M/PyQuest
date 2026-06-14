from engine.inputs import random_word, random_int


def random_text():
    lines = []
    for _ in range(random_int(1, 4)):
        words = [random_word(2, 7) for _ in range(random_int(1, 4))]
        lines.append(" ".join(words))
    return "".join(line + "\n" for line in lines)


def check(T):
    T.run(files={"in.txt": "quiet please\n"})
    T.eq(T.file("out.txt"), "QUIET PLEASE",
         because="out.txt should hold in.txt uppercased.")

    T.run(files={"in.txt": ""})
    T.eq(T.file("out.txt"), "",
         because="An empty input makes an empty output, not a crash.")

    for _ in range(8):
        text = random_text()
        T.run(files={"in.txt": text})
        T.eq(T.file("out.txt"), text.upper(),
             because="Every character of in.txt, uppercased, in out.txt.")
    T.uses_with_open(because="Open both files with `with open(...) as f:`.")
