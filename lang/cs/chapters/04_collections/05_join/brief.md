# 4.5 -- join: seznam na text

## Koncept

`.join()` je opak `split`: slepí **seznam řetězců** do jednoho řetězce a mezi každý
kousek vloží oddělovač. Voláš ho *na oddělovači*:

```python
words = ["a", "b", "c"]
print("-".join(words))    # a-b-c
print(", ".join(words))   # a, b, c
print("".join(words))     # abc   (no separator)
```

Čti to jako „spoj tato slova s tímto oddělovačem mezi nimi“. Seznam musí obsahovat
řetězce.

## Častá chyba

`join` se píše oddělovačem napřed: `"-".join(words)`, **ne** `words.join("-")`.

## Příklad

```python
parts = ["2024", "12", "25"]
print("/".join(parts))    # 2024/12/25
```

## Tvůj úkol

Přečti počet `n`, pak `n` slov (jedno na řádek), do seznamu. Vypiš je spojená
pomlčkou `-`.

Pro vstup `3`, pak `a`, `b`, `c`:

```
a-b-c
```

## Hotovo, když

- `a, b, c` vypíše `a-b-c`; jedno slovo vypíše jen to slovo.
- Počet `0` vypíše prázdný řádek (není co spojovat).
