Objekty **spolupracují**: metoda může brát **jiný objekt** téže třídy jako
parametr, číst jeho atributy a **vrátit nový** objekt držící výsledek — přičemž oba
vstupy nechá beze změny.

- `def add(self, other):` sáhne na `self.x` a `other.x`, pak
  `return Vector(self.x + other.x, ...)`. Vrácení čerstvé instance drží operandy
  neměnné.
- Takto se skládají hodnotové objekty (body, vektory, peníze). Definice dunderu
  `__add__` by dokonce nechala `a + b` ji zavolat.

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)

Vector(1, 2).add(Vector(3, 4)).x    # 4
```
