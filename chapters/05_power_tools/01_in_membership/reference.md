The **`in`** operator tests membership and yields a boolean, so it drops straight
into an `if` or `while`. `x in c` is `True` when `x` is found in `c`.

- For a **string**, `in` tests for a **substring**: `"cat" in "concatenate"` is
  `True`.
- For a **list** or **tuple**, it tests for an item (scanning the sequence).
- For a **dict** or **set**, it tests for a **key**/member — and is fast
  (hash-based), unlike the linear scan of a list.
- `x not in c` is the readable negation.

```python
"a" in "cat"          # True
3 in [1, 2, 3]        # True
"key" in {"key": 1}   # True  -- tests keys
```
