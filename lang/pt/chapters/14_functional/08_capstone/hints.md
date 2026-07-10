Três passos. Primeiro, `filter(lambda r: r[1] >= threshold, records)` mantém
os registos que se qualificam (r[1] é a pontuação).

---

Depois, `sorted(qualified, key=lambda r: r[1], reverse=True)` classifica-os
do mais alto para o mais baixo, e `map(lambda r: r[0], ...)` extrai os nomes.
Envolve o map em `list`.

---

def passing(records, threshold):
    qualified = filter(lambda r: r[1] >= threshold, records)
    ranked = sorted(qualified, key=lambda r: r[1], reverse=True)
    return list(map(lambda r: r[0], ranked))
