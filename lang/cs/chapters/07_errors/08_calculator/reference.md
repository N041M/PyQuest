Po jediném `try` může následovat **několik klauzulí `except`**, každá ošetřuje jiné
selhání svou vlastní reakcí. Testují se shora dolů; spustí se **první**
odpovídající typ a zbytek se přeskočí.

- Tím se staví odolné zpracování vstupu: jeden `try` kolem práce, pak `except` na
  každou věc, která se může pokazit (`ValueError` pro špatné číslo,
  `ZeroDivisionError` pro `/0`), každý s vlastní zprávou.
- Řaď od konkrétního k obecnému, jsou-li typy příbuzné, protože vítězí první
  shoda.

```python
try:
    a, b = int(x), int(y)
    print(a / b)
except ValueError:
    print("please enter whole numbers")
except ZeroDivisionError:
    print("cannot divide by zero")
```
