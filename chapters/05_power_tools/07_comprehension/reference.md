A **list comprehension** builds a new list in one expression: for each `x` in
`items`, it evaluates `expr` and collects the results, in order. It is the
build-by-loop-and-append pattern compressed into a line.

- `[expr for x in items]` is equivalent to starting `result = []` and
  `result.append(expr)` in a loop — same result, more direct.
- `expr` can be any expression in `x`: `[n * n for n in nums]`,
  `[w.upper() for w in words]`.
- Comprehensions also build sets (`{...}`) and dicts (`{k: v for ...}`).

```python
[n * n for n in range(5)]       # [0, 1, 4, 9, 16]
[w.upper() for w in ["a", "b"]] # ['A', 'B']
```
