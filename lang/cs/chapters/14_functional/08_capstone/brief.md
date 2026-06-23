# 14.8 -- Závěrečná: seřazený užší výběr

## Koncept

Nástroje kapitoly se zřetězí do **potrubí** (pipeline). Daný seznam záznamů
`(name, score)` sestav užší výběr:

1. **`filter`** na záznamy, které splní práh,
2. **`sorted`** s `key=lambda` (a `reverse=True`), abys je seřadil od nejvyššího po
   nejnižší,
3. **`map`** ven jen jména.

```python
records = [("Ada", 90), ("Linus", 70), ("Grace", 95)]
qualified = filter(lambda r: r[1] >= 80, records)
ranked = sorted(qualified, key=lambda r: r[1], reverse=True)
list(map(lambda r: r[0], ranked))     # ['Grace', 'Ada']
```

Každý záznam je n-tice, takže `r[0]` je jméno a `r[1]` skóre.

## Tvůj úkol

Definuj `passing(records, threshold)`, která bere seznam n-tic `(name, score)` a
vrátí **jména** těch se `score >= threshold`, seřazená podle skóre **od nejvyššího**,
sestavená pomocí `filter`, `sorted(key=lambda ...)` a `map`.

## Hotovo, když

- `passing([("Ada", 90), ("Linus", 70), ("Grace", 95)], 80)` vrátí
  `["Grace", "Ada"]`.
- `passing([], 50)` vrátí `[]`; práh nad každým skóre vrátí `[]`.
- Výsledek je sestaven filtrováním, řazením podle lambda klíče a mapováním -- potrubí
  nástrojů kapitoly.
