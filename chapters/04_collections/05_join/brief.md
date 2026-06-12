# 4.5 -- join: a list into text

## Concept

`.join()` is the opposite of `split`: it glues a **list of strings** into one
string, putting a separator between each piece. You call it *on the separator*:

```python
words = ["a", "b", "c"]
print("-".join(words))    # a-b-c
print(", ".join(words))   # a, b, c
print("".join(words))     # abc   (no separator)
```

Read it as "join these words with this separator between them". The list must
contain strings.

## Common mistake

`join` is written separator-first: `"-".join(words)`, **not** `words.join("-")`.

## Example

```python
parts = ["2024", "12", "25"]
print("/".join(parts))    # 2024/12/25
```

## Your task

Read a count `n`, then `n` words (one per line), into a list. Print them joined
with a dash `-`.

For input `3`, then `a`, `b`, `c`:

```
a-b-c
```

## Done when

- `a, b, c` prints `a-b-c`; a single word prints just that word.
- A count of `0` prints an empty line (nothing to join).
