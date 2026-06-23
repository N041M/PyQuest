# 3.5 -- and / or / not

## Koncept

Booleany můžeš kombinovat třemi slovy:

- `and` -- True jen když jsou **obě** strany True.
- `or` -- True když je True **alespoň jedna** strana.
- `not` -- otočí boolean: `not True` je `False`.

```python
print(True and False)   # False
print(True or False)    # True
print(not True)         # False

age = 25
print(age >= 18 and age < 65)   # True  (both hold)
```

Díky tomu může jedna podmínka testovat několik věcí najednou.

## Příklad

```python
n = 12
print(n % 2 == 0 and n % 3 == 0)   # True  (12 is divisible by both)
```

## Tvůj úkol

Přečti celé číslo. Vypiš, zda je dělitelné **zároveň** 2 i 3 -- tedy vypiš výsledek
`(n % 2 == 0) and (n % 3 == 0)` (což je `True`, nebo `False`).

Pro vstup `12` je výstup:

```
True
```

## Hotovo, když

- `12` a `6` vypíšou `True`; `4` a `9` vypíšou `False`.
- `0` vypíše `True` (0 je dělitelná vším).
