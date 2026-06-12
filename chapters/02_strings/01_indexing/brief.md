# 2.1 -- Indexing

## Concept

A string is a sequence of characters, and each character has a **position**
(called an *index*). Counting starts at **0**, not 1. So in the string `"cat"`:

```
character:  c  a  t
index:      0  1  2
```

You read a single character with square brackets: `s[index]`.

```python
word = "cat"
print(word[0])   # c
print(word[1])   # a
```

`word[0]` is the first character, because indexing starts at zero. This trips up
almost everyone at first: the "first" character lives at index 0.

## Example

```python
s = "python"
print(s[0])   # p
```

## Your task

Read a word with `input()`, then print only its **first** character.

For input `hello` the output is:

```
h
```

## Done when

- For `hello` it prints `h`.
- It works for any word, including a single-letter word (the checker tries a
  few).
