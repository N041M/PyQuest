Read ALL the names into one list first, then all the scores into another --
only then pair them.

---

`for name, score in zip(names, scores):` gives one pair per pass; print the
two with a space between (plain `print(name, score)` does that).

---

n = int(input())
names = []
for _ in range(n):
    names.append(input())
scores = []
for _ in range(n):
    scores.append(input())
for name, score in zip(names, scores):
    print(name, score)
