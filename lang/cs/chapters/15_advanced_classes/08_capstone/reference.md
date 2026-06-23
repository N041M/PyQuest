Závěrečná úloha smísí kapitolu do jedné hierarchie, tak, jak se skutečné třídy
staví:

- **Dědičnost** — `Rectangle(Shape)` *je* `Shape`, takže dostane `describe` zadarmo a
  `isinstance(r, Shape)` je pravda.
- **`super()`** — `Rectangle.__init__` volá `super().__init__("rectangle")`, aby
  základ nastavil `self.name`, pak přidá vlastní šířku a výšku.
- **`@property`** — `area` se počítá ze šířky a výšky při každém přístupu, takže
  zůstává správná, když se strana změní.
- **Polymorfismus** — `Shape.describe` čte `self.area`, který definuje jen
  `Rectangle`; metoda základu funguje skrz property podtřídy.
- **Dundery** — `__eq__` a `__lt__` (oba podle obsahu) dělají z obdélníků věci, které
  se porovnávají a řadí jako vestavěné hodnoty, takže `==` a `sorted` prostě fungují.

Dohromady tyto promění prostý objekt na takový, který se chová jako prvotřídní
hodnota: má identitu v hierarchii, odvozená data a smysluplnou rovnost a uspořádání
— odměnu celé kapitoly.

```python
r = Rectangle(3, 4)
r.describe()                              # 'rectangle with area 12'
Rectangle(2, 6) == Rectangle(3, 4)        # True  -- equal areas
sorted([Rectangle(3, 4), Rectangle(1, 1)])   # by area: 1, then 12
```
