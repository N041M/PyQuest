Pro každou dvojici přečti dvě čísla a přidej je jako dvoupoložkový seznam [a, b].

---

`pairs.append([a, b])` staví vnořený seznam. Vypiš ho, pak projdi:
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
