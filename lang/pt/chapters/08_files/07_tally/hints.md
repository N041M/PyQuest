Lê as palavras para uma lista, depois constrói um dicionário de contagens com
o padrão `counts[w] = counts.get(w, 0) + 1` de 5.9.

---

Para ordenar o relatório, ordena as chaves do dicionário com uma função
`key`: `sorted(counts, key=lambda w: (-counts[w], w))` dá a contagem mais alta
primeiro, alfabética dentro dos empates. Escreve cada
`f"{w}: {counts[w]}\n"`.

---

with open("words.txt") as f:
    words = f.read().split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
with open("report.txt", "w") as f:
    for w in sorted(counts, key=lambda w: (-counts[w], w)):
        f.write(f"{w}: {counts[w]}\n")
