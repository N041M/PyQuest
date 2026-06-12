# 2.2 -- Negative indexing

## Concept

You can also count from the **end** of a string using negative indexes. `-1` is
the last character, `-2` the second-to-last, and so on.

```
character:   c   a   t
index:       0   1   2
from end:   -3  -2  -1
```

```python
word = "cat"
print(word[-1])   # t
print(word[-2])   # a
```

This is handy when you do not want to count the length: `s[-1]` is always the
last character, no matter how long the string is.

## Example

```python
s = "python"
print(s[-1])   # n
```

## Your task

Read a word, then print its **last** character.

For input `hello` the output is:

```
o
```

## Done when

- For `hello` it prints `o`.
- It works for a single-letter word too (`-1` points at that one character).
