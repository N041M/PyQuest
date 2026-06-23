# 15.8 -- Závěrečná: hierarchie tvarů

## Koncept

Stáhni kapitolu do jedné malé hierarchie. Základní `Shape` drží jméno a umí se
popsat; `Rectangle` z něj dědí, přidá velikost, spočítá svůj obsah jako property a
porovnává se s jinými obdélníky podle obsahu.

```python
class Shape:
    def __init__(self, name):
        self.name = name
    def describe(self):
        return "%s with area %d" % (self.name, self.area)   # uses the property

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height
    @property
    def area(self):
        return self.width * self.height
    def __eq__(self, other):
        return self.area == other.area
    def __lt__(self, other):
        return self.area < other.area
```

Všimni si, že `Shape.describe` používá `self.area`, který definuje jen `Rectangle`
-- metoda základu funguje skrz property podtřídy (polymorfismus).

## Tvůj úkol

Postav přesně dvě výše uvedené třídy:

- `Shape.__init__(self, name)` a `describe(self)` -> `"<name> with area <area>"`.
- `Rectangle(Shape)`: `__init__(self, width, height)` nastaví jméno na
  `"rectangle"` přes `super()`, uloží width/height; property `area`; a
  `__eq__` / `__lt__` porovnávající podle `area`.

## Hotovo, když

- `Rectangle(3, 4).area` je `12`; `.name` je `"rectangle"`; `.describe()` je
  `"rectangle with area 12"`; je to `Shape`.
- `Rectangle(2, 6) == Rectangle(3, 4)` je `True` (stejné obsahy).
- `sorted([Rectangle(3, 4), Rectangle(1, 1), Rectangle(2, 5)])` je seřazeno podle
  obsahu (1, 10, 12).
