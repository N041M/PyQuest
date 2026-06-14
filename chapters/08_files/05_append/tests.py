from engine.inputs import random_word, random_int


def random_log():
    lines = [random_word(2, 7) for _ in range(random_int(1, 5))]
    return "".join(w + "\n" for w in lines)


def check(T):
    # No log.txt seeded: append mode CREATES the file. A solution that reads
    # the file before rewriting it would crash here -- "a" must not pre-read.
    T.run(stdin="hello\n")
    T.eq(T.file("log.txt"), "hello",
         because="Append mode creates log.txt when it doesn't exist yet.")

    T.run(stdin="ran\n", files={"log.txt": "woke up\nate\n"})
    T.eq(T.file("log.txt"), "woke up\nate\nran",
         because="The old lines stay; the new entry is appended.")

    T.run(stdin="first\n", files={"log.txt": ""})
    T.eq(T.file("log.txt"), "first",
         because="Appending to an empty file just writes the line.")

    for _ in range(8):
        original = random_log()
        entry = random_word(3, 9)
        T.run(stdin=entry + "\n", files={"log.txt": original})
        T.eq(T.file("log.txt"), original + entry + "\n",
             because="%r appended to the existing log, nothing erased."
                     % entry)
