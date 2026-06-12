# 2.3 -- Slicing

## Concept

A **slice** takes a range of characters at once: `s[start:stop]`. It includes the
character at `start` and goes **up to but not including** `stop`. This is called
*half-open*: the stop index is not included.

```python
s = "python"
print(s[0:3])   # pyt   (indexes 0, 1, 2 -- not 3)
print(s[2:5])   # tho   (indexes 2, 3, 4)
```

Leave out `start` and it begins at 0; leave out `stop` and it runs to the end:

```python
print(s[:3])    # pyt   (same as s[0:3])
print(s[3:])    # hon   (from index 3 to the end)
```

Because the stop is not included, `s[0:3]` gives you exactly **3** characters.

## Example

```python
s = "rainbow"
print(s[0:4])   # rain
```

## Your task

Read a word, then print its **first three** characters.

For input `hello` the output is:

```
hel
```

## Done when

- For `hello` it prints `hel`.
- For a word shorter than three letters it prints the whole word -- slicing past
  the end is safe and does not error. The checker tries `hi`.
