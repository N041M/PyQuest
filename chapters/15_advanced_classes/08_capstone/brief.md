# 15.8 -- Capstone: a shape hierarchy

## Concept

Pull the chapter together into one small hierarchy. A base `Shape` holds a name
and can describe itself; a `Rectangle` inherits from it, adds size, computes its
area as a property, and compares to other rectangles by area.

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

Notice `Shape.describe` uses `self.area`, which only `Rectangle` defines -- the
base method works through the subclass's property (polymorphism).

## Your task

Build exactly the two classes above:

- `Shape.__init__(self, name)` and `describe(self)` -> `"<name> with area
  <area>"`.
- `Rectangle(Shape)`: `__init__(self, width, height)` sets the name to
  `"rectangle"` via `super()`, stores width/height; an `area` **property**; and
  `__eq__` / `__lt__` comparing by `area`.

## Done when

- `Rectangle(3, 4).area` is `12`; `.name` is `"rectangle"`; `.describe()` is
  `"rectangle with area 12"`; it is a `Shape`.
- `Rectangle(2, 6) == Rectangle(3, 4)` is `True` (equal areas).
- `sorted([Rectangle(3, 4), Rectangle(1, 1), Rectangle(2, 5)])` is ordered by
  area (1, 10, 12).
