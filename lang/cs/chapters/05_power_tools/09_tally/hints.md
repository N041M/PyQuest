Rozděl řádek na seznam slov, pak ho projdi a stav sčítací slovník.

---

Sčítací řádek je  counts[w] = counts.get(w, 0) + 1  -- a konečná odpověď je další
.get s výchozí hodnotou: counts.get(query, 0).

---

words = input().split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
query = input()
print(counts.get(query, 0))
