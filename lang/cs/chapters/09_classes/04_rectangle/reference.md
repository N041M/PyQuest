Třída může držet **několik atributů** a nabízet **několik metod**, které nad nimi
spolupracují — modelujíce něco s více než jednou vlastností.

- `__init__` uloží každý kus dat (`self.width`, `self.height`); každá metoda čte
  atributy, které potřebuje.
- Metody mohou stavět na stejných datech pro různé odpovědi: `area` násobí,
  `perimeter` sčítá — jeden objekt, mnoho otázek.
- Držet data a operace v jedné třídě znamená, že se volající ptají objektu, místo
  aby žonglovali s volnými proměnnými.

```python
class Rectangle:
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):      return self.w * self.h
    def perimeter(self): return 2 * (self.w + self.h)

r = Rectangle(3, 4); r.area(), r.perimeter()   # (12, 14)
```
