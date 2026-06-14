Read the entry with `input()`, then open the file in a mode that *keeps* what
is already there.

---

Mode `"a"` appends instead of wiping. Don't forget the `"\n"` so the new entry
sits on its own line.

---

entry = input()
with open("log.txt", "a") as f:
    f.write(entry + "\n")
