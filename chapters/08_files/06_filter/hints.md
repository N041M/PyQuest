Read all the lines first, then open the output file in `"w"` mode and loop,
writing only the ones you want to keep.

---

`if line.strip():` is true only when the line has real content. Write the
original `line` (it already ends in `\n`), not a stripped copy.

---

with open("lines.txt") as f:
    lines = f.readlines()
with open("kept.txt", "w") as f:
    for line in lines:
        if line.strip():
            f.write(line)
