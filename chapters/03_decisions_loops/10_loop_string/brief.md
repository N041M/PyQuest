# 3.10 -- Looping over a string

## Concept

A `for` loop works on more than ranges. A **string is a sequence of characters**,
so you can loop straight over it -- one character per pass:

```python
for ch in "cat":
    print(ch)
# prints:
# c
# a
# t
```

No indexing needed: `ch` is each character in turn. (You can loop over many kinds
of sequences this way; strings are the first.)

## Example

```python
word = "hi"
for ch in word:
    print(ch)
# prints h then i
```

## Your task

Read a word and print each of its characters on its own line, using a `for`
loop over the string.

For input `cat` the output is:

```
c
a
t
```

## Done when

- `cat` prints `c`, `a`, `t` on separate lines.
- A single letter prints that letter; empty input prints nothing.
