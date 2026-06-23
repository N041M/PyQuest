# 15.6 -- __eq__: rovnost podle hodnoty

## Koncept

Ve výchozím stavu se `==` na objektech ptá „jsou to **tentýž objekt**?“ -- takže dva
samostatně postavené objekty se stejnými daty si *nejsou* rovné. Dunder metoda
**`__eq__`** to změní na **rovnost podle hodnoty**:

```python
class Money:
    def __init__(self, cents):
        self.cents = cents
    def __eq__(self, other):
        return self.cents == other.cents

Money(500) == Money(500)     # True   -- same value
Money(500) == Money(750)     # False
```

- Python volá `a.__eq__(b)` pro `a == b`. Vrátíš, zda se mají počítat jako rovné --
  obvykle porovnáním atributů, které definují hodnotu.
- `!=` se vyřeší za tebe (je to negace `__eq__`).
- (Definice `__eq__` je také to, co umožní porovnávat tvé objekty podle hodnoty v
  testech, seznamech a kontrolách `in`.)

## Tvůj úkol

Definuj `Money` s `__init__(self, cents)` a **`__eq__`** tak, aby si dva objekty
`Money` byly rovné právě tehdy, když se shodují jejich `cents`.

## Hotovo, když

- `Money(500) == Money(500)` je `True`.
- `Money(500) == Money(750)` je `False`.
- Rovnost porovnává `cents`, ne identitu objektu.
