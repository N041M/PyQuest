Divide a linha numa lista de palavras, depois percorre-a construindo o dicionário de contagem.

---

A linha de contagem é  counts[w] = counts.get(w, 0) + 1  -- e a resposta final é
outro .get com um valor por omissão: counts.get(query, 0).

---

words = input().split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
query = input()
print(counts.get(query, 0))
