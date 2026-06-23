# 3.3 -- if / else

## Koncept

`else` dá `if` druhou větev: kód, který se spustí, když je podmínka **False**.
Spustí se přesně jeden ze dvou bloků.

```python
if temperature > 30:
    print("hot")
else:
    print("not hot")
```

`else:` je zarovnané s `if` (stejné odsazení) a jeho blok je odsazený stejně jako
blok `if`.

## Připomenutí

`n % 2` je zbytek po dělení `n` dvěma (s `%` ses setkal v kapitole 1). Číslo je
**sudé** právě tehdy, když `n % 2 == 0`.

## Příklad

```python
n = 7
if n % 2 == 0:
    print("even")
else:
    print("odd")
# prints: odd
```

## Tvůj úkol

Přečti celé číslo a vypiš `even`, je-li sudé, nebo `odd`, pokud není.

Pro vstup `10` je výstup:

```
even
```

## Hotovo, když

- Sudá čísla vypíšou `even`, lichá `odd`.
- Funguje pro `0` (sudá) i pro záporná čísla.
