# 4.4 -- split: text into a list

## Concept

`s.split()` breaks a string into a **list of pieces**. With no argument it splits
on whitespace, so it turns a sentence into its words:

```python
"the quick brown fox".split()    # ['the', 'quick', 'brown', 'fox']
```

The result is a real list, so everything you know about lists applies -- `len`,
indexing, looping:

```python
words = "a b c".split()
print(len(words))    # 3
print(words[0])      # a
```

You can also split on a specific separator by passing it in:
`"a,b,c".split(",")` gives `['a', 'b', 'c']`.

## Example

```python
parts = "one two three".split()
print(len(parts))    # 3
```

## Your task

Read a line of words separated by spaces, and print **how many words** it
contains.

For input `the quick brown fox`:

```
4
```

## Done when

- `the quick brown fox` prints `4`; a single word prints `1`.
- An empty line prints `0`.
