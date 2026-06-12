# 2.5 -- Steps and reversing

## Concept

A slice can take a third number, the **step**: `s[start:stop:step]`. The step says
how many positions to move each time. A step of `2` takes every second character:

```python
s = "abcdef"
print(s[::2])   # ace   (every 2nd character)
```

A **negative** step walks backwards. The shortcut `s[::-1]` -- empty start, empty
stop, step `-1` -- reverses the whole string:

```python
s = "python"
print(s[::-1])   # nohtyp
```

`s[::-1]` is the standard Python way to reverse a string.

## Example

```python
print("hello"[::-1])   # olleh
```

## Your task

Read a word, then print it **reversed**.

For input `hello` the output is:

```
olleh
```

## Done when

- For `hello` it prints `olleh`.
- For a single letter, or a word that reads the same backwards (like `level`), it
  prints the word unchanged. The checker tries both.
