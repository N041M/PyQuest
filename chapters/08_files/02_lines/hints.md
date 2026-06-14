A file object is iterable: `for line in f:` hands you one line per pass.

---

`enumerate(f, start=1)` gives `(1, firstline), (2, secondline), ...`. Each line
still ends in `\n` -- use `line.strip()` to drop it.

---

with open("tasks.txt") as f:
    for i, line in enumerate(f, start=1):
        print(f"{i}. {line.strip()}")
