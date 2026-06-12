For each pair, read two numbers and append them as a two-item list [a, b].

---

`pairs.append([a, b])` builds the nested list. Print it, then loop:
`for p in pairs: print(p[0] + p[1])`.

---

n = int(input())
pairs = []
for _ in range(n):
    a = int(input())
    b = int(input())
    pairs.append([a, b])
print(pairs)
for p in pairs:
    print(p[0] + p[1])
