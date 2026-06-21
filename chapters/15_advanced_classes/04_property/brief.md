# 15.4 -- @property: a computed attribute

## Concept

Sometimes a value is **derived** from others -- a rectangle's area from its width
and height. You could store it, but then it goes stale when width changes. A
**`@property`** computes it on every access, while still being read like a plain
attribute:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

r = Rectangle(3, 4)
r.area        # 12   -- no parentheses, but the method runs
r.width = 5
r.area        # 20   -- recomputed from the new width
```

- `@property` above a method makes `obj.area` (no `()`) call that method and
  return its result.
- Because it runs each time, the value is always current -- unlike a value stored
  once in `__init__`.

## Your task

Define `Rectangle` with `__init__(self, width, height)` and an **`area`**
**property** that returns `width * height`.

## Done when

- `Rectangle(3, 4).area` is `12` (accessed with no parentheses).
- After `r = Rectangle(3, 4); r.width = 5`, `r.area` is `20` -- recomputed, not
  stored.
