# 1.7 -- Text vs. číslo

## Koncept

Python rozlišuje dva druhy hodnot a hodně na tom záleží:

- **Číslo** jako `5` -- psané bez uvozovek. Celým číslům Python říká `int`
  (integer).
- **Řetězec** jako `"5"` -- psaný s uvozovkami. Je to *text*, který jen náhodou
  vypadá jako číslo. Python mu říká `str`.

Se znakem `+` se chovají odlišně:

- U čísel `+` **sčítá**: `5 + 5` je `10`.
- U řetězců `+` **spojuje** (tomu se říká **zřetězení**): `"5" + "5"` je `"55"` --
  dva kusy textu slepené dohromady.

```python
print(5 + 5)        # 10   (numbers add)
print("5" + "5")    # 55   (text joins)
print("ab" + "cd")  # abcd
```

Takže `"5"` a `5` vypadají na obrazovce stejně, ale jsou to různé typy a `+` s
nimi zachází úplně jinak.

## Častý omyl

`"5"` není číslo pět. Uvozovky z toho dělají text. Nemůžeš s ním počítat a čekat
sčítání -- `"5" + "5"` dá `"55"`, ne `10`.

## Tvůj úkol

Vypiš tyto dva řádky, v tomto pořadí:

```
55
10
```

- První řádek musí vzniknout **spojením dvou řetězců** `"5"` a `"5"` pomocí `+`.
- Druhý řádek musí vzniknout **sečtením dvou čísel** `5` a `5` pomocí `+`.

## Hotovo, když

- Výstup je `55` a pak `10`.
- První řádek používá zřetězení řetězců; druhý řádek používá sčítání čísel.
