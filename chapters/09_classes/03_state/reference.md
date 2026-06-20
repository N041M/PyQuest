An object holds **state** — data that persists between calls. A method can
**mutate** `self`, and the next method call sees the change, so the object
remembers what happened to it.

- `self.count += 1` updates an attribute in place; the new value lives on until
  changed again.
- This is the point of objects: they carry their data with them across calls,
  unlike a plain function whose locals vanish when it returns.
- Each instance has its **own** copy of the attributes, so two counters count
  independently.

```python
class Counter:
    def __init__(self):
        self.n = 0
    def tick(self):
        self.n += 1         # remembered for next time

c = Counter(); c.tick(); c.tick(); c.n   # 2
```
