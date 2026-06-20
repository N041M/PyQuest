**`min(items)`** and **`max(items)`** return the smallest and largest item of a
non-empty collection.

- They compare with `<`/`>`, so they work on numbers and on strings (which
  compare lexicographically).
- Called on an **empty** iterable they raise `ValueError`; pass `default=` to
  supply a fallback.
- A `key=` function ranks by a derived value instead of the item itself:
  `max(words, key=len)` returns the **longest** word.

```python
min([3, 1, 4])             # 1
max("apple", "pear")       # 'pear'
max(words, key=len)        # the longest word
```
