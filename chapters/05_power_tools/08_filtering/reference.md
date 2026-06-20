Adding an **`if`** to a comprehension keeps only the items that pass the test.
`[x for x in items if test]` collects each `x` for which `test` is true,
**skipping** the rest.

- The `if` clause filters; the leading expression still transforms, so the two
  combine: `[n * n for n in nums if n % 2 == 0]` squares only the evens.
- It replaces the loop-with-an-`if`-and-`append` pattern.
- Don't confuse it with a **conditional expression** in the value position
  (`[a if cond else b for x in items]`), which chooses per item rather than
  filtering.

```python
[n for n in range(10) if n % 2 == 0]   # [0, 2, 4, 6, 8]
[w for w in words if len(w) > 3]       # only long words
```
