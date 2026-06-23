**Metoda** je funkce definovaná uvnitř třídy. Vždy bere **`self`** první a počítá z
vlastních atributů objektu, takže chování žije s daty, na nichž působí.

- Voláš ji `instance.metoda()`; Python instanci automaticky předá jako `self`,
  takže `p.dist()` volá `dist(p)`.
- Uvnitř dosáhneš na data objektu skrze `self`: `self.x`, `self.y`.
- Metoda může brát další parametry za `self` a `return` hodnotu jako každá funkce.

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def dist(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

Point(3, 4).dist()      # 5.0
```
