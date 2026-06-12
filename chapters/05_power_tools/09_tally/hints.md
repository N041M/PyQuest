Split the line into a list of words, then loop over it building the tally dict.

---

The tally line is  counts[w] = counts.get(w, 0) + 1  -- and the final answer is
another .get with a default: counts.get(query, 0).

---

words = input().split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
query = input()
print(counts.get(query, 0))
