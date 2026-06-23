# 4.6 -- Seznamy v seznamech

## Koncept

Seznam může držet **jiné seznamy**. Takto reprezentuješ řádky dat, dvojice, mřížky
a podobně:

```python
pairs = [[1, 2], [3, 4], [5, 6]]
print(pairs)        # [[1, 2], [3, 4], [5, 6]]
print(pairs[0])     # [1, 2]        the first inner list
print(pairs[0][1])  # 2            first inner list, second item
```

Dva indexy: první vybere vnitřní seznam, druhý vybere položku uvnitř něj.
Procházení ti postupně dá každý vnitřní seznam:

```python
for p in pairs:
    print(p[0] + p[1])   # 3, 7, 11
```

## Příklad

```python
grid = [[1, 1], [2, 2]]
for row in grid:
    print(row[0] + row[1])   # 2, 4
```

## Tvůj úkol

Přečti počet `n`, pak `n` **dvojic** čísel (každá dvojice jsou dvě čísla na dvou
řádcích). Sestav seznam dvojic `[a, b]`. Nejprve vypiš celý vnořený seznam, pak
vypiš **součet každé dvojice**, jeden na řádek.

Pro vstup `2`, pak `1`, `2`, `3`, `4`:

```
[[1, 2], [3, 4]]
3
7
```

## Hotovo, když

- `1,2` a `3,4` vypíšou `[[1, 2], [3, 4]]` pak `3` pak `7`.
- Počet `0` vypíše `[]` a nic víc.
