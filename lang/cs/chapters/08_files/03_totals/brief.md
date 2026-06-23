# 8.3 -- Sčítání souboru

## Koncept

Soubor je vždy **text**. Řádek, který vypadá jako `42`, dorazí jako řetězec
`"42\n"`, ne jako číslo 42 -- takže než můžeš počítat, musíš ho převést pomocí
`int()` (1.11), přesně jako jsi to dělal s `input()`.

`int()` rád ignoruje okolní bílé znaky, takže `int("42\n")` je `42` -- ani nemusíš
nejdřív ořezávat.

```python
total = 0
with open("prices.txt") as f:
    for line in f:
        total += int(line)
```

## Příklad

Pro `prices.txt` ve tvaru:

```
10
25
7
```

je součet `42`.

## Tvůj úkol

`prices.txt` drží jedno celé číslo na řádek. Přečti je, všechna je sečti a vypiš
součet.

## Hotovo, když

- Program vypíše součet každého čísla v souboru.
- Záporná čísla i jednořádkový soubor fungují.
- Soubor jsi otevřel pomocí `with` a každý řádek převedl pomocí `int()`.
