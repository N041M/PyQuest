A `with open(name) as f:` block gives you the file as `f`. Inside it, ask the
file for everything it holds.

---

`f.read()` returns the whole file as a single string. Store it, then print it
after (or inside) the block.

---

with open("note.txt") as f:
    text = f.read()
print(text)
