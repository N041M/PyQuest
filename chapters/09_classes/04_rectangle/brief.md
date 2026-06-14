# 9.4 -- More data, more methods

## Concept

A class can hold several pieces of data and offer several methods over them.
Nothing new in the syntax -- just more of it:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
```

Both methods read the same stored data through `self`; each Rectangle answers
either question about itself:

```python
r = Rectangle(3, 4)
r.area()        # 12
r.perimeter()   # 14
```

## Your task

Define a class `Rectangle` whose `__init__` stores a `width` and a `height`,
with two methods: `area()` returns `width * height`, and `perimeter()` returns
`2 * (width + height)`.

## Done when

- `Rectangle(3, 4).area()` is `12` and `.perimeter()` is `14`.
- Both work for any width and height.
- Both are methods on the class, computing from `self`.
