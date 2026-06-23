**`__lt__(self, other)`** definuje operátor **`<`** pro tvé objekty a `<` je přesně
to, co **`sorted`**, **`min`** a **`max`** používají k řazení věcí. Bez něj porovnání
dvou tvých objektů vyvolá `TypeError`; s ním se seznam z nich řadí přímo.

- Python volá `a.__lt__(b)` pro `a < b`; vrať, zda má `a` přijít **před** `b`,
  obvykle porovnáním atributu, podle něhož řadíš.
- `sorted` potřebuje jen `<`, takže samotné `__lt__` udělá objekty řaditelnými. Úplná
  sada řadicích dunderů je `__lt__`, `__le__`, `__gt__`, `__ge__`.
- `functools.total_ordering` je dekorátor třídy, který doplní zbylé tři z `__lt__` a
  `__eq__`, pokud chceš všechna porovnání.

```python
class Temperature:
    def __init__(self, degrees): self.degrees = degrees
    def __lt__(self, other): return self.degrees < other.degrees

sorted([Temperature(30), Temperature(10), Temperature(20)])   # 10, 20, 30
min([Temperature(30), Temperature(10)]).degrees               # 10
```
