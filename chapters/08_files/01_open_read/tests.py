from engine.inputs import random_word, random_int


def random_text(rng_lines=(1, 5), rng_words=(1, 5)):
    lines = []
    for _ in range(random_int(*rng_lines)):
        words = [random_word(2, 7) for _ in range(random_int(*rng_words))]
        lines.append(" ".join(words))
    return "".join(line + "\n" for line in lines)


def check(T):
    T.eq(T.run(files={"note.txt": "buy milk\ncall sam\n"}),
         "buy milk\ncall sam",
         because="Read and print the file's whole contents.")
    T.eq(T.run(files={"note.txt": "just one line\n"}), "just one line")
    T.eq(T.run(files={"note.txt": ""}), "",
         because="An empty file prints nothing -- no crash.")
    for _ in range(8):
        text = random_text()
        T.eq(T.run(files={"note.txt": text}), text,
             because="Whatever note.txt holds should come back out.")
    T.uses_with_open(because="Open the file with `with open(...) as f:`.")
