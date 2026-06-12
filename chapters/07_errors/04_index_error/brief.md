# 7.4 -- IndexError and safe access

## Concept

Indexing past the end of a list raises `IndexError`:

```python
items = ["a", "b"]
items[5]      # IndexError!
```

A "safe get" returns a fallback instead of crashing -- and it is another
place where *trying* beats *pre-testing*. Remember that negative indexes are
**valid** (2.2): `items[-1]` is the last item, `items[-2]` the one before.
A hand-written bounds check has to get `0 <= i`... no wait, `-len <= i <
len`... exactly right, in two directions. Or you just try it:

```python
try:
    return items[i]
except IndexError:
    return default
```

The `except` is correct *by definition* -- it fires precisely when Python
itself says the index is bad, negatives included.

## Example

```python
item_or(["a", "b"], 0, "?")     # "a"
item_or(["a", "b"], -1, "?")    # "b"   -- valid negative index
item_or(["a", "b"], 5, "?")     # "?"   -- out of range, fallback
```

## Your task

Define `item_or(items, i, default)` that returns `items[i]`, or `default`
when `i` is out of range -- using `try`/`except IndexError`.

## Done when

- `item_or(["a", "b"], 1, "?")` is `"b"`; index `5` gives `"?"`.
- `item_or(["a", "b"], -1, "?")` is `"b"` -- negatives that fit are valid.
- `item_or([], 0, "?")` is `"?"` -- an empty list has no valid index.
- You used `try`/`except` -- bounds arithmetic dodges the lesson and fails.
