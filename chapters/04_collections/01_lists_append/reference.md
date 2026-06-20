A **list** is an ordered, mutable sequence of values, written in square brackets:
`[10, 20, 30]`. The empty list is `[]`. Items are reached by index just like
string characters (`lst[0]`, `lst[-1]`).

- **`.append(x)`** adds `x` to the **end**, growing the list by one. It changes
  the list in place and returns `None` (so never write `lst = lst.append(x)`).
- The build-from-empty pattern: start with `[]`, then `.append` once per pass of
  a loop to collect results.
- Unlike strings, a list may hold values of mixed types.

```python
nums = []
for i in range(3):
    nums.append(i * i)   # -> [0, 1, 4]
```
