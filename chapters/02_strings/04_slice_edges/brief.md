# 2.4 -- Slicing the middle

## Concept

Slicing mixes happily with negative indexes, and slices never crash -- if a slice
is empty, you simply get the empty string `""`.

`s[1:-1]` means "from index 1 up to (but not including) the last character" -- in
other words, drop the first and last characters:

```python
s = "python"
print(s[1:-1])   # ytho
```

If the string is too short to have a middle, the slice is just empty:

```python
print("ab"[1:-1])   # (nothing -- an empty string)
print("a"[1:-1])    # (nothing)
```

No error. An empty slice is a normal, valid result.

## Common misconception

Going "out of range" with a slice does **not** crash, unlike indexing a single
character. `"hi"[5]` would be an error, but `"hi"[1:5]` is fine -- it just stops
at the end.

## Example

```python
s = "hello"
print(s[1:-1])   # ell
```

## Your task

Read a word, then print it **without its first and last characters**.

For input `hello` the output is:

```
ell
```

## Done when

- For `hello` it prints `ell`.
- For a 1- or 2-letter word it prints an empty line (no middle) and does not
  crash. The checker tries `ab` and `a`.
