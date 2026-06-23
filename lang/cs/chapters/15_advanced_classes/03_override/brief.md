# 15.3 -- Přepsání: vlastní verze potomka

## Koncept

Podtřída může **přepsat** (override) rodičovu metodu -- definovat vlastní verzi
metody, kterou rodič už má. Pro instance podtřídy vítězí nová verze:

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "..."          # generic

class Cat(Animal):
    def speak(self):
        return "Meow"         # Cat's own
```

- `Cat("Felix").speak()` vrátí `"Meow"`; prosté `Animal(...).speak()` stále vrátí
  `"..."`.
- To je **polymorfismus**: *stejné* volání, `x.speak()`, udělá správnou věc pro
  jakýkoli typ, jímž `x` je.
- Podtřída stále dědí vše, co nepřepíše (zde `__init__` a `self.name`).

## Tvůj úkol

Definuj `Animal` s `__init__(self, name)` a `speak(self)` vracejícím `"..."`. Pak
definuj `Cat(Animal)`, který **přepíše** `speak`, aby vracelo `"Meow"`.

## Hotovo, když

- `Cat("Felix").speak()` vrátí `"Meow"`.
- `Animal("thing").speak()` vrátí `"..."` (beze změny).
- `Cat("Felix").name` je `"Felix"` (zděděný `__init__`) a Cat je Animal.
