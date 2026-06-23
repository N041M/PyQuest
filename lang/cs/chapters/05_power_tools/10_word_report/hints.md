Tři kroky: rozděl řádek, sečti slova (5.9), pak vypiš -- a `sorted(counts)` dá
klíče slovníku v abecedním pořadí.

---

Po sčítacím cyklu:  `for w in sorted(counts): print(w, counts[w])`.

---

words = input().split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
for w in sorted(counts):
    print(w, counts[w])
