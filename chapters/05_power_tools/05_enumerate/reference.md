**`enumerate(items)`** pairs each item with its position, so a `for` loop gets
both at once — no hand-kept counter.

- `for i, item in enumerate(lst):` binds `i` to the index (from 0) and `item` to
  the value each pass.
- A second argument sets the **starting number**: `enumerate(lst, 1)` numbers
  from 1, handy for human-facing lists.
- It's lazy (yields pairs on demand) and works on any iterable.

```python
for i, name in enumerate(["a", "b"], 1):
    print(i, name)        # 1 a / 2 b
```
