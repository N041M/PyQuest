Objekt souboru je iterovatelný: `for line in f:` ti podá jeden řádek na průchod.

---

`enumerate(f, start=1)` dá `(1, prvnířádek), (2, druhýřádek), ...`. Každý řádek
stále končí na `\n` -- použij `line.strip()`, abys ho zahodil.

---

with open("tasks.txt") as f:
    for i, line in enumerate(f, start=1):
        print(f"{i}. {line.strip()}")
