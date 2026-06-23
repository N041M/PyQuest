# 4.1 -- Seznamy a append

## Koncept

**Seznam** drží několik hodnot v pořadí v jedné proměnné. Seznam zapíšeš hranatými
závorkami, položky oddělené čárkami:

```python
nums = [10, 20, 30]
print(nums)        # [10, 20, 30]
print(nums[0])     # 10   (index like a string -- from 0)
print(len(nums))   # 3
```

Seznam může začít prázdný a růst. `.append(x)` přidá `x` na **konec**:

```python
nums = []
nums.append(10)
nums.append(20)
print(nums)        # [10, 20]
```

Tento vzor „začni prázdný, přidávej v cyklu“ je způsob, jak sestavit seznam ze
vstupu.

## Příklad

```python
items = []
items.append(1)
items.append(2)
print(items)       # [1, 2]
```

## Tvůj úkol

Přečti celé číslo `n`, pak přečti dalších `n` celých čísel (jedno na řádek).
Posbírej je do seznamu pomocí `.append()` a vypiš hotový seznam.

Pro vstup `3`, pak `1`, `2`, `3`:

```
[1, 2, 3]
```

## Hotovo, když

- `3` s `1, 2, 3` vypíše `[1, 2, 3]`.
- Počet `0` vypíše `[]` (prázdný seznam).
