# 4.11 -- Množiny

## Koncept

**Množina** (set) je neuspořádaná kolekce **jedinečných** položek -- automaticky
zahazuje duplicity. Zapíšeš ji složenými závorkami, nebo sestavíš ze seznamu pomocí
`set(...)`:

```python
s = {1, 2, 2, 3}
print(s)              # {1, 2, 3}   (the duplicate 2 is gone)

nums = [1, 1, 2, 3, 3]
print(set(nums))      # {1, 2, 3}
print(len(set(nums))) # 3           how many *distinct* values
```

Množiny jsou skvělé pro „kolik různých věcí?“ a pro rychlé testy příslušnosti
pomocí `in`:

```python
print(2 in s)         # True
```

(Množiny nemají pořadí ani indexování -- nemůžeš udělat `s[0]`.)

## Příklad

```python
words = ["a", "b", "a"]
print(len(set(words)))   # 2
```

## Tvůj úkol

Přečti počet `n`, pak `n` slov. Vypiš, kolik je **odlišných** slov.

Pro vstup `4`, `a`, `b`, `a`, `c`:

```
3
```

(`a` se objeví dvakrát, ale počítá se jednou.)

## Hotovo, když

- `a, b, a, c` vypíše `3`.
- Počet `0` vypíše `0`.
