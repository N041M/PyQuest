# 14.6 -- all: are they every one true?

## Concept

**`all(iterable)`** is `any`'s partner: it returns `True` only if **every** item
is truthy. It answers "do they *all* pass?":

```python
all(n > 0 for n in [1, 2, 3])      # True
all(n > 0 for n in [1, -2, 3])     # False
```

- It **short-circuits** the other way: it stops and returns `False` at the first
  item that fails.
- `all([])` is `True` -- vacuously, since no item failed. (A common surprise:
  "all of nothing" is true.)

Same shape as `any`: `all(<test> for <item> in <iterable>)`.

## Example

```python
def all_words(strings):
    return all(s.isalpha() for s in strings)
```

## Your task

Using **`all`**, define `all_positive(nums)` that returns `True` if **every**
number in `nums` is greater than zero.

## Done when

- `all_positive([1, 2, 3])` is `True`; `all_positive([1, -2, 3])` is `False`.
- `all_positive([])` is `True` (nothing fails).
- The answer comes from `all(...)`, not a hand-written loop with a flag.
