# 14.5 -- any: is at least one true?

## Concept

**`any(iterable)`** returns `True` if **at least one** item is truthy, `False`
otherwise. Fed a generator of tests, it answers "does *any* item pass?":

```python
any(n < 0 for n in [1, 2, -3])     # True
any(n < 0 for n in [1, 2, 3])      # False
```

- It replaces the loop-with-a-flag (`found = False; for ...: if ...: found =
  True`) with one expression.
- It **short-circuits**: it stops and returns `True` at the first truthy item.
- `any([])` is `False` (nothing passed).

The pattern is `any(<test> for <item> in <iterable>)` -- a generator expression
of booleans handed to `any`.

## Example

```python
def has_blank(strings):
    return any(s == "" for s in strings)
```

## Your task

Using **`any`**, define `has_negative(nums)` that returns `True` if `nums`
contains at least one negative number.

## Done when

- `has_negative([1, 2, -3])` is `True`; `has_negative([1, 2, 3])` is `False`.
- `has_negative([])` is `False`.
- The answer comes from `any(...)`, not a hand-written loop with a flag.
