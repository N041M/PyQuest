# 9.5 -- Printing an object: `__str__`

## Concept

Print an object as-is and you get something useless like
`<__main__.Point object at 0x10f3d2b80>`. To control how an object looks as
text, define the special method `__str__`, which returns the string Python
should show.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
```

`__str__` is a **dunder** (double-underscore) method -- Python calls it for you
whenever the object is turned into text, by `print()` or `str()`:

```python
p = Point(3, 4)
print(p)        # (3, 4)
str(p)          # "(3, 4)"
```

You never call `__str__` yourself; you just define it, and `str(p)` triggers it.

## Your task

Define a class `Point` storing `x` and `y`, with a `__str__` method so that
`str(Point(3, 4))` is exactly `"(3, 4)"` -- the two values in parentheses,
comma-and-space between them.

## Done when

- `str(Point(3, 4))` is `"(3, 4)"`.
- It works for any `x` and `y`, including negatives.
- The formatting comes from a `__str__` method on the class.
