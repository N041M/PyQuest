A string is **iterable**, so a `for` loop walks it **one character at a time**,
in order, binding the loop variable to each character. You don't index by hand.

- Each pass gives a one-character string; the loop runs `len(s)` times.
- This is the direct way to examine or tally characters — pair it with an `if`
  inside the loop to act on certain ones.
- The same `for ... in` form iterates any sequence (lists, ranges, …), not just
  strings.

```python
for ch in "cat":
    print(ch)             # c, then a, then t
```
