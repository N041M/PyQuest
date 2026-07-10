# 15.8 -- Capstone: uma hierarquia de formas

## Conceito

Junta o capítulo todo numa pequena hierarquia. Uma classe base `Shape` guarda
um nome e sabe descrever-se; um `Rectangle` herda dela, acrescenta tamanho,
calcula a sua área como propriedade, e compara-se com outros retângulos pela
área.

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

Repara que `Shape.describe` usa `self.area`, que só `Rectangle` define -- o
método da base funciona através da propriedade da subclasse (polimorfismo).

## A tua tarefa

Constrói exatamente as duas classes acima:

- `Shape.__init__(self, name)` e `describe(self)` -> `"<name> with area
  <area>"`.
- `Rectangle(Shape)`: `__init__(self, width, height)` define o nome como
  `"rectangle"` via `super()`, guarda width/height; uma **propriedade**
  `area`; e `__eq__` / `__lt__` a comparar por `area`.

## Está feito quando

- `Rectangle(3, 4).area` é `12`; `.name` é `"rectangle"`; `.describe()` é
  `"rectangle with area 12"`; é um `Shape`.
- `Rectangle(2, 6) == Rectangle(3, 4)` é `True` (áreas iguais).
- `sorted([Rectangle(3, 4), Rectangle(1, 1), Rectangle(2, 5)])` fica ordenado
  pela área (1, 10, 12).
