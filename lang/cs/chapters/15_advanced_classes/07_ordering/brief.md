# 15.7 -- __lt__: učiň objekty řaditelnými

## Koncept

`sorted`, `min` i `max` všechny řadí věci pomocí operátoru **`<`**. Ve výchozím
stavu Python neví, jak porovnat dva tvé objekty -- jejich řazení vyvolá `TypeError`.
Definuj **`__lt__`** („less than“, menší než) a stanou se řaditelnými:

```python
class Temperature:
    def __init__(self, degrees):
        self.degrees = degrees
    def __lt__(self, other):
        return self.degrees < other.degrees

temps = [Temperature(30), Temperature(10), Temperature(20)]
sorted(temps)        # ordered 10, 20, 30 -- by degrees
```

- Python volá `a.__lt__(b)` pro `a < b`. Vrátíš, zda má `a` přijít **před** `b` --
  obvykle porovnáním atributu, podle něhož chceš řadit.
- `sorted` potřebuje jen `<`, takže samotné `__lt__` udělá seznam tvých objektů
  řaditelným.

## Tvůj úkol

Definuj `Temperature` s `__init__(self, degrees)` a **`__lt__`** tak, aby se teploty
porovnávaly podle `degrees`.

## Hotovo, když

- `Temperature(10) < Temperature(20)` je `True`.
- `sorted([Temperature(30), Temperature(10), Temperature(20)])` je seřazeno
  `10, 20, 30` podle stupňů.
- Porovnání používá `degrees`.
