# 9.2 -- Methods: behaviour on the data

## Concept

Objects don't just hold data -- they have **methods**, functions that live on
the object and work with its own data through `self`.

```python
class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
```

`area` is a method: it takes `self` (the object it's called on) and uses
`self.side`. You call it with a dot and parentheses -- no need to pass `self`,
Python fills it in:

```python
s = Square(5)
print(s.area())   # 25
```

The point of a method is that the behaviour travels *with* the data: any Square
already knows how to compute its own area.

## Your task

Define a class `Square` whose `__init__` stores a `side`, and add a method
`area()` that returns the square's area (`side * side`).

## Done when

- `Square(5).area()` returns `25`.
- It works for any side length, including `0`.
- `area` is a method on the class and computes from `self.side`.
