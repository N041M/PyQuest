Read the words into a list, then build a dict of counts with the
`counts[w] = counts.get(w, 0) + 1` pattern from 5.9.

---

To order the report, sort the dict's keys with a key function:
`sorted(counts, key=lambda w: (-counts[w], w))` gives highest count first,
alphabetical within ties. Write each `f"{w}: {counts[w]}\n"`.

---

with open("words.txt") as f:
    words = f.read().split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
with open("report.txt", "w") as f:
    for w in sorted(counts, key=lambda w: (-counts[w], w)):
        f.write(f"{w}: {counts[w]}\n")
