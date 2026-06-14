Two steps: first read in.txt into a string, then open out.txt in `"w"` mode and
write the uppercased string.

---

`open("out.txt", "w")` is the write half; `text.upper()` does the uppercasing.
`.write()` writes the string as-is.

---

with open("in.txt") as f:
    text = f.read()
with open("out.txt", "w") as f:
    f.write(text.upper())
