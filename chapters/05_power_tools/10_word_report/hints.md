Three steps: split the line, tally the words (5.9), then print -- and
`sorted(counts)` gives the dict's keys in alphabetical order.

---

After the tally loop:  `for w in sorted(counts): print(w, counts[w])`.

---

words = input().split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
for w in sorted(counts):
    print(w, counts[w])
