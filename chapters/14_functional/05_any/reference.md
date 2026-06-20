**`any(iterable)`** returns `True` as soon as **one** item is truthy, else
`False`. Handed a generator of tests, it answers "does any item pass?" in a single
expression, replacing a loop that sets a flag.

- It **short-circuits**: evaluation stops at the first truthy item, so it's
  efficient and works on infinite/lazy iterables.
- `any([])` is `False` — there is nothing to be true.
- The idiom is `any(<test> for <item> in <iterable>)`: a generator expression of
  booleans. (Its partner `all` is 14.6.)

```python
any(n < 0 for n in [1, 2, -3])    # True
any(c.isdigit() for c in "abc")   # False
any([])                           # False
```
