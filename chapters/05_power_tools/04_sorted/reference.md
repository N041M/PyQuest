**`sorted(items)`** returns a **new** list with the items in ascending order,
leaving the original untouched.

- It accepts any iterable and always returns a list. Numbers sort numerically,
  strings lexicographically.
- **`reverse=True`** sorts descending. **`key=`** sorts by a derived value:
  `sorted(words, key=len)` orders by length, `sorted(d.items(), key=lambda kv:
  kv[1])` orders dict pairs by value.
- The list method `lst.sort()` sorts **in place** and returns `None`; use
  `sorted` when you want a new list or are sorting a non-list.

```python
sorted([3, 1, 2])               # [1, 2, 3]
sorted([3, 1, 2], reverse=True) # [3, 2, 1]
sorted(words, key=len)          # shortest to longest
```
