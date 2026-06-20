# 11.5 -- Counter: tally in one step

## Concept

Back in chapter 5 you tallied by hand: `counts[k] = counts.get(k, 0) + 1`. The
**`collections`** module ships that pattern, written and tested, as **`Counter`**:

```python
from collections import Counter

Counter("banana")     # Counter({'a': 3, 'n': 2, 'b': 1})
```

- `Counter(items)` walks any iterable and returns a count of each distinct item.
- A `Counter` **is** a dict (it's a subclass), so `counts[x]` and
  `for k, v in counts.items()` work exactly as you'd expect -- and it compares
  equal to the plain dict with the same counts.
- It even handles the missing key: `counts["zzz"]` is `0`, not a `KeyError`.

This is the standard library's promise: the loop you'd write is already a tool.

## Example

```python
from collections import Counter

def letter_counts(word):
    return Counter(word)
```

## Your task

Using **`Counter`** from `collections`, define `tally(items)` that returns a
count of how many times each item appears in the list `items`.

## Done when

- `tally(["a", "b", "a"])` equals `{"a": 2, "b": 1}`.
- `tally([])` equals `{}`.
- The counting is done by `Counter`, not a hand-written loop.
