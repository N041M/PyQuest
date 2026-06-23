# 1.9 -- Tři druhy dělení

## Koncept

Dělení má v Pythonu tři užitečné operátory:

- `/`  běžné dělení -- vždy dá desetinné číslo (Python jim říká `float`). `7 / 2`
  je `3.5`.
- `//` celočíselné dělení -- vydělí a zahodí desetinnou část, takže dá celé číslo.
  `7 // 2` je `3`.
- `%`  modulo -- dá **zbytek** po dělení. `7 % 2` je `1` (protože 2 se do 7 vejde
  třikrát a 1 zbude).

```python
print(7 / 2)    # 3.5
print(7 // 2)   # 3
print(7 % 2)    # 1
```

Číslo s desetinnou tečkou, jako `3.5`, je `float`. Celé číslo bez tečky, jako `3`,
je `int`. Všimni si, že `/` dá `3.5`, i když dělí čísla vypadající beze zbytku:
`4 / 2` je `2.0`, ne `2`.

`%` je překvapivě šikovné: číslo je sudé právě tehdy, když `n % 2` je `0`.

## Častý omyl

`/` nezaokrouhluje na celé číslo. `7 / 2` je `3.5`, nikdy `3`. Pokud chceš
celočíselnou část, od toho je `//`.

## Tvůj úkol

Pomocí čísel 7 a 2 vypiš tyto tři řádky v pořadí:

```
3.5
3
1
```

Pro první použij `/`, pro druhý `//` a pro třetí `%`.

## Hotovo, když

- Výstup je přesně `3.5`, pak `3`, pak `1`.
- Každý řádek používá odpovídající operátor (`/`, `//`, `%`).
