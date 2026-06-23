**Třída** definuje nový typ objektu a svazuje související data do jedné hodnoty.
**`__init__`** je inicializátor: Python ho zavolá automaticky, když vytváříš
instanci, aby nastavil její počáteční data.

- `class Point:` otevře definici; volání `Point(3, 4)` vytvoří **instanci** a
  spustí `__init__`.
- **`self`** je instance, která se staví; `self.x = x` uloží hodnotu jako
  **atribut** na ni, kde ji každá metoda později dosáhne.
- První parametr `__init__` je vždy `self`; zbytek jsou argumenty, které volající
  předá.

```python
class Point:
    def __init__(self, x, y):
        self.x = x          # store data on the instance
        self.y = y

p = Point(3, 4)
p.x                         # 3
```
