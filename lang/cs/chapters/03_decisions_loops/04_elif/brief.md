# 3.4 -- elif

## Koncept

`elif` (zkratka za „else if“) přidá **další větve** mezi `if` a `else`. Python
kontroluje podmínky popořadě a spustí **první**, která je `True`; ostatní přeskočí.
`else` (volitelné) zachytí vše, co zbylo.

```python
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
```

Na pořadí záleží: protože vítězí první pravdivá větev, obvykle postupuješ od
nejkonkrétnější nebo nejvyšší podmínky dolů.

## Příklad

```python
n = 0
if n < 0:
    print("negative")
elif n == 0:
    print("zero")
else:
    print("positive")
# prints: zero
```

## Tvůj úkol

Přečti celé číslo a vypiš přesně jedno z:

- `negative`, je-li menší než 0,
- `zero`, je-li 0,
- `positive`, je-li větší než 0.

Pro vstup `0` je výstup:

```
zero
```

## Hotovo, když

- `-3` vypíše `negative`, `0` vypíše `zero`, `5` vypíše `positive`.
- Pro libovolný vstup se vypíše přesně jeden řádek.
