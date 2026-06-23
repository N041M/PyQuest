# 8.7 -- Zpráva o četnosti

## Koncept

Tato úloha spojuje kapitolu se slovníkovým sčítáním z 5.9: přečti soubor, **spočítej**
v něm něco a výsledek zapiš do jiného souboru.

Načti slova, pak je sečti slovníkem (vzor `dict.get`):

```python
with open("words.txt") as f:
    words = f.read().split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
```

`f.read().split()` přečte celý soubor a rozdělí podle libovolných bílých znaků,
takže ti podá plochý seznam slov, ať byla rozmístěna jakkoli.

Pak zapiš zprávu, **seřazenou podle počtu, nejvyšší první**, shody řešené abecedně.
`sorted` s `key` (5.4) udělá obojí najednou:

```python
for w in sorted(counts, key=lambda w: (-counts[w], w)):
    f.write(f"{w}: {counts[w]}\n")
```

Klíč `(-counts[w], w)` řadí podle sestupného počtu (znegovaného) a pak podle
samotného slova u shod.

## Příklad

`words.txt` ve tvaru `fig fig pear fig pear` se stane `report.txt` ve tvaru:

```
fig: 3
pear: 2
```

## Tvůj úkol

Spočítej, jak často se každé slovo objeví ve `words.txt`, a zapiš `report.txt` s
jedním řádkem `slovo: počet` na každé odlišné slovo -- seřazeným podle počtu
(nejvyšší první), shody v abecedním pořadí.

## Hotovo, když

- Každé odlišné slovo se objeví jednou, jako `slovo: počet`.
- Řádky jsou seřazeny podle sestupného počtu, abecedně v rámci shody.
- Použil jsi `with`, slovník ke sčítání a přečetl slova ze souboru.
