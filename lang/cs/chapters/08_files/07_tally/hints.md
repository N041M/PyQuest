Načti slova do seznamu, pak sestav slovník počtů vzorem
`counts[w] = counts.get(w, 0) + 1` z 5.9.

---

K seřazení zprávy seřaď klíče slovníku s klíčovou funkcí:
`sorted(counts, key=lambda w: (-counts[w], w))` dá nejvyšší počet první, abecedně
v rámci shod. Zapiš každé `f"{w}: {counts[w]}\n"`.

---

with open("words.txt") as f:
    words = f.read().split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
with open("report.txt", "w") as f:
    for w in sorted(counts, key=lambda w: (-counts[w], w)):
        f.write(f"{w}: {counts[w]}\n")
