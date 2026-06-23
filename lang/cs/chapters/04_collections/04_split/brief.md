# 4.4 -- split: text na seznam

## Koncept

`s.split()` rozdělí řetězec na **seznam kousků**. Bez argumentu dělí podle bílých
znaků, takže větu promění na její slova:

```python
"the quick brown fox".split()    # ['the', 'quick', 'brown', 'fox']
```

Výsledek je skutečný seznam, takže platí vše, co o seznamech víš -- `len`,
indexování, procházení:

```python
words = "a b c".split()
print(len(words))    # 3
print(words[0])      # a
```

Můžeš také dělit podle konkrétního oddělovače tím, že ho předáš:
`"a,b,c".split(",")` dá `['a', 'b', 'c']`.

## Příklad

```python
parts = "one two three".split()
print(len(parts))    # 3
```

## Tvůj úkol

Přečti řádek slov oddělených mezerami a vypiš, **kolik slov** obsahuje.

Pro vstup `the quick brown fox`:

```
4
```

## Hotovo, když

- `the quick brown fox` vypíše `4`; jedno slovo vypíše `1`.
- Prázdný řádek vypíše `0`.
