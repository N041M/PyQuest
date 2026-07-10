Um objeto de ficheiro é iterável: `for line in f:` dá-te uma linha por
passagem.

---

`enumerate(f, start=1)` dá `(1, primeiralinha), (2, segundalinha), ...`. Cada
linha ainda termina em `\n` -- usa `line.strip()` para a remover.

---

with open("tasks.txt") as f:
    for i, line in enumerate(f, start=1):
        print(f"{i}. {line.strip()}")
