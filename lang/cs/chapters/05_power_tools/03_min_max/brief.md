# 5.3 -- min() a max()

## Koncept

Najít nejmenší nebo největší položku je další cyklus, který bys mohl napsat ručně
(„drž si dosud nejlepší, porovnávej každou položku“) -- a další cyklus, který Python
dodává jako vestavěný:

```python
nums = [3, 7, 1]
print(min(nums))    # 1
print(max(nums))    # 7
```

`min()` a `max()` vezmou seznam (vlastně jakoukoli neprázdnou kolekci) a vrátí jeho
nejmenší / největší položku. Fungují i na řetězcích -- „nejmenší“ pak znamená
nejdřívější v abecedním pořadí:

```python
min("cab")     # "a"
```

Jedno upozornění: u **prázdného** seznamu spadnou (z ničeho není nejmenší), takže
tato úloha zaručuje alespoň jedno číslo.

## Příklad

```python
nums = [4, -2, 9]
print(min(nums))    # -2
print(max(nums))    # 9
```

## Tvůj úkol

Přečti počet `n` (vždy alespoň 1), pak `n` celých čísel. Vypiš dva řádky: nejmenší,
pak největší.

Pro vstup `3`, pak `4`, `-2`, `9`:

```
-2
9
```

## Hotovo, když

- `4, -2, 9` vypíše `-2` pak `9`.
- Jediné číslo vypíše samo sebe dvakrát (je zároveň min i max).
- Použil jsi `min()` a `max()`.
