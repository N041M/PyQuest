Indexing past the end of a list (or string) raises **`IndexError`**. Catching it
turns a risky lookup into a **safe access** that returns a fallback when the
position doesn't exist.

- `lst[i]` raises if `i >= len(lst)` (or `i < -len(lst)`); the `except` supplies a
  default instead of crashing.
- This is the EAFP counterpart to checking `if i < len(lst):` first — useful when
  the out-of-range case is normal rather than a bug.

```python
def get(lst, i, default=None):
    try:
        return lst[i]
    except IndexError:
        return default   # position absent -> fallback
```
