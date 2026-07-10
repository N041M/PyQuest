Um conjunto descarta duplicados. Coloca as palavras num conjunto, e depois conta-o.

---

Reúne as palavras numa lista, depois `print(len(set(words)))`.

---

n = int(input())
words = []
for _ in range(n):
    words.append(input())
print(len(set(words)))
