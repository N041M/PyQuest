# 9.5 -- Tisk objektu: `__str__`

## Koncept

Vypiš objekt tak, jak je, a dostaneš něco nepoužitelného jako
`<__main__.Point object at 0x10f3d2b80>`. Abys řídil, jak objekt vypadá jako text,
definuj speciální metodu `__str__`, která vrátí řetězec, jejž má Python zobrazit.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
```

`__str__` je **dunder** (metoda s dvojitým podtržítkem) -- Python ji za tebe zavolá,
kdykoli se objekt mění na text, pomocí `print()` nebo `str()`:

```python
p = Point(3, 4)
print(p)        # (3, 4)
str(p)          # "(3, 4)"
```

`__str__` nikdy nevoláš sám; jen ji definuješ a `str(p)` ji spustí.

## Tvůj úkol

Definuj třídu `Point` ukládající `x` a `y`, s metodou `__str__` tak, aby
`str(Point(3, 4))` bylo přesně `"(3, 4)"` -- dvě hodnoty v závorkách, mezi nimi
čárka a mezera.

## Hotovo, když

- `str(Point(3, 4))` je `"(3, 4)"`.
- Funguje pro libovolné `x` a `y`, včetně záporných.
- Formátování pochází z metody `__str__` na třídě.
