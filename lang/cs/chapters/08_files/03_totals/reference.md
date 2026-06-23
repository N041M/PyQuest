Obsah souboru je vždy **text**, takže řádek jako `"42\n"` je *řetězec*. Abys mohl
počítat, musíš každý řádek nejprve převést na číslo.

- `int(line)` rozparsuje celé číslo; toleruje okolní bílé znaky (včetně koncového
  zalomení), takže `int("42\n")` je `42`. Pro desetinná použij `float(line)`.
- Prázdný nebo nečíselný řádek vyvolá `ValueError` — přeskoč prázdné
  (`if not line.strip(): continue`) nebo obal převod do `try`.
- Akumuluj průběžně: drž průběžný součet a přičítej každou rozparsovanou hodnotu.

```python
total = 0
with open("nums.txt") as f:
    for line in f:
        total += int(line)    # text -> number, then add
```
