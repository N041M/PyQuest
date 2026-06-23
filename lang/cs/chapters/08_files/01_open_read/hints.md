Blok `with open(name) as f:` ti dá soubor jako `f`. Uvnitř něj požádej soubor o
vše, co drží.

---

`f.read()` vrátí celý soubor jako jeden řetězec. Ulož ho, pak ho vypiš po (nebo
uvnitř) bloku.

---

with open("note.txt") as f:
    text = f.read()
print(text)
