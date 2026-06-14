# 9.3 -- State that remembers

## Concept

An object's data lives **between** method calls -- a method can change `self`,
and the next call sees the change. That's what makes objects useful: they
*remember*.

```python
class Counter:
    def __init__(self):
        self.count = 0

    def tick(self):
        self.count = self.count + 1
        return self.count
```

Each `tick()` bumps `self.count` and hands back the new value:

```python
c = Counter()
c.tick()   # 1
c.tick()   # 2
c.tick()   # 3
```

Crucially, the count lives **on the instance** (`self.count`), so two counters
keep separate tallies -- ticking one never touches the other.

## Your task

Define a class `Counter` that starts its `count` at `0`. Add a method `tick()`
that adds one to the count and **returns the new count**.

## Done when

- A fresh `Counter` ticked three times returns `1`, `2`, `3`.
- Two counters are independent -- ticking one doesn't change the other.
- The count is stored on `self`, not shared across all counters.
