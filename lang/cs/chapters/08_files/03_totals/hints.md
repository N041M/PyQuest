Začni průběžný součet na 0, otevři soubor a procházej jeho řádky.

---

Každý řádek je řetězec jako `"25\n"`. `int(line)` z něj udělá číslo, které můžeš
přičíst. Po cyklu vypiš součet.

---

total = 0
with open("prices.txt") as f:
    for line in f:
        total += int(line)
print(total)
