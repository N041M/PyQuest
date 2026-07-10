Três passos: divide a linha, conta as palavras (5.9), depois imprime -- e
`sorted(counts)` dá as chaves do dicionário em ordem alfabética.

---

Depois do ciclo de contagem:  `for w in sorted(counts): print(w, counts[w])`.

---

words = input().split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
for w in sorted(counts):
    print(w, counts[w])
