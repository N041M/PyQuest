Para cada par, lê dois números e acrescenta-os como uma lista de dois itens [a, b].

---

`pairs.append([a, b])` constrói a lista aninhada. Imprime-a, depois percorre num
ciclo: `for p in pairs: print(p[0] + p[1])`.

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
