Závěrečná úloha čte **záznamy**, každý rozparsuje na použitelná pole, seřadí je a
zapíše **naformátovanou zprávu** — podobu skutečné datové práce.

- **Parsuj**: rozděl každý řádek na pole a převeď typy (např.
  `name, score = line.split(","); score = int(score)`), přičemž záznamy sbíráš do
  seznamu.
- **Seřaď**: `sorted(records, key=..., reverse=True)` seřadí podle pole, na kterém
  záleží.
- **Naformátuj**: zapiš zarovnané, čitelné řádky pomocí šířek polí f-řetězce
  (`f"{name:<12}{score:>5}"`), aby sloupce lícovaly.

```python
records = []
with open("scores.csv") as f:
    for line in f:
        name, score = line.strip().split(",")
        records.append((name, int(score)))
with open("ranked.txt", "w") as out:
    for name, score in sorted(records, key=lambda r: r[1], reverse=True):
        out.write(f"{name:<12}{score:>5}\n")
```
