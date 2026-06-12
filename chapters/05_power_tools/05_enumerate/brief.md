# 5.5 -- enumerate()

## Concept

Sometimes a loop needs both the **item** and its **position**. You could track
a counter by hand, but Python has a built-in for exactly this:

```python
words = ["tea", "milk"]
for i, w in enumerate(words):
    print(i, w)
# 0 tea
# 1 milk
```

Each pass, `enumerate` hands you a pair `(position, item)`, which you unpack
into two variables (4.7) -- the same trick as `for k, v in d.items()`.

Counting from `0` is rarely what you want to *show* a person. The second
argument sets the starting number:

```python
for i, w in enumerate(words, 1):
    print(i, w)
# 1 tea
# 2 milk
```

## Example

```python
for i, ch in enumerate("hi", 1):
    print(f"{i}. {ch}")
# 1. h
# 2. i
```

## Your task

Read a count `n`, then `n` words. Print them as a numbered list starting at 1,
in the format `1. word` (a dot and a space after the number).

For input `3`, then `tea`, `milk`, `sugar`:

```
1. tea
2. milk
3. sugar
```

## Done when

- Three words print as `1. ...`, `2. ...`, `3. ...`.
- A count of `0` prints nothing.
- You used `enumerate()` -- no hand-kept counter.
