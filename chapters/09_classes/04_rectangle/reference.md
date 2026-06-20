A class can hold **several attributes** and offer **several methods** that work
together over them — modelling something with more than one property.

- `__init__` stores each piece of data (`self.width`, `self.height`); each method
  reads whatever attributes it needs.
- Methods can build on the same data for different answers: `area` multiplies,
  `perimeter` adds — one object, many questions.
- Keeping the data and the operations in one class means callers ask the object
  rather than juggling loose variables.

```python
class Rectangle:
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):      return self.w * self.h
    def perimeter(self): return 2 * (self.w + self.h)

r = Rectangle(3, 4); r.area(), r.perimeter()   # (12, 14)
```
