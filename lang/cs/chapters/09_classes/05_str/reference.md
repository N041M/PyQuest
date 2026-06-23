**`__str__`** definuje čitelný text pro objekt. Když instanci `print`neš nebo na ni
zavoláš `str()`, Python zavolá `__str__` a použije to, co vrátí.

- Bez ní vypsání objektu ukáže neužitečnou výchozí podobu jako
  `<Point object at 0x...>`; `__str__` to nahradí něčím smysluplným.
- Musí **vrátit** řetězec (ne ho vypsat), obvykle sestavený f-řetězcem z atributů
  objektu.
- `__str__` je jedna z několika **dunder** („dvojité podtržítko“) metod, které
  Python volá za tebe, jako `__init__`.

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __str__(self):
        return f"({self.x}, {self.y})"

print(Point(3, 4))      # (3, 4)
```
