# 1.8 -- Aritmetika a pořadí

## Koncept

Python počítá pomocí těchto znaků (zvaných **operátory**):

- `+` sčítání
- `-` odčítání
- `*` násobení
- `/` dělení

```python
print(2 + 3)   # 5
print(10 - 4)  # 6
print(6 * 7)   # 42
```

**Na pořadí záleží.** Stejně jako ve školní matematice se `*` a `/` provádějí
**před** `+` a `-`. Takže:

```python
print(2 + 3 * 4)   # 14, not 20  -- 3*4 first, then +2
```

Chceš-li vynutit jiné pořadí, obal část do **závorek** `( )`. Cokoli je uvnitř
závorek, vyhodnotí se nejdřív:

```python
print((2 + 3) * 4)   # 20  -- 2+3 first, then *4
```

Tohle je vůbec nejčastější zdroj chyb typu „špatné číslo“, takže se vyplatí si to
teď osvojit.

## Příklad

```python
print(1 + 2 * 3)     # 7
print((1 + 2) * 3)   # 9
```

## Tvůj úkol

Vypiš tyto dva řádky:

```
14
20
```

- První řádek je `2 + 3 * 4` bez závorek (nejdřív násobení).
- Druhý řádek jsou stejná čísla, ale se závorkami, aby se nejdřív sčítalo:
  `(2 + 3) * 4`.

## Hotovo, když

- Výstup je `14` a pak `20`.
- Rozdíl mezi řádky vzniká pouze tím, že závorky mění pořadí.
