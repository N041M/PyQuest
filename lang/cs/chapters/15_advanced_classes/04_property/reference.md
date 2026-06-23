**`@property`** je dekorátor, který promění metodu na **počítaný atribut jen pro
čtení**. `obj.area` (bez závorek) spustí metodu a vrátí její výsledek, takže
odvozená hodnota se přepočítá při každém přístupu a nikdy nezastará.

- Skryje fakt, že se děje práce: volající používají `obj.area`, ne `obj.area()`,
  přesně jako u uloženého atributu — ale hodnota vždy odráží aktuální stav.
- Holé `@property` je jen pro čtení; přiřazení do něj vyvolá `AttributeError`. Přidej
  odpovídající `@area.setter`, abys umožnil přiřazení s validací.
- Dej property přednost před hodnotou uloženou v `__init__`, kdykoli hodnota
  *závisí* na jiných atributech, které se mohou změnit.

```python
class Rectangle:
    def __init__(self, w, h): self.width, self.height = w, h
    @property
    def area(self): return self.width * self.height

r = Rectangle(3, 4)
r.area        # 12
r.width = 5
r.area        # 20  -- recomputed
```
