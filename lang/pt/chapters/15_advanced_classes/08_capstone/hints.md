Começa com `Shape`: `__init__(self, name)` e `describe` a devolver
`"%s with area %d" % (self.name, self.area)`. Isto refere-se a `self.area`,
que a subclasse vai fornecer.

---

`Rectangle(Shape)`: no `__init__` chama `super().__init__("rectangle")`,
guarda width/height; acrescenta `@property area` a devolver
`width * height`; acrescenta `__eq__` e `__lt__` que comparam `self.area` com
`other.area`.

---

class Shape:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return "%s with area %d" % (self.name, self.area)


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
