**`sep.join(parts)`** glues an iterable of **strings** into one string, placing
`sep` between adjacent items. The separator is the string you call it on, which
reads oddly at first but lets the separator be any string.

- Every item must already be a string; numbers raise `TypeError`. Convert first,
  e.g. `", ".join(str(n) for n in nums)`.
- `"".join(parts)` concatenates with no separator — the efficient way to build a
  string from many pieces (far better than repeated `+`).
- It is the inverse of `split`.

```python
"-".join(["2024", "01", "15"])   # '2024-01-15'
" ".join(["the", "fox"])          # 'the fox'
```
