# 8.3 -- Adding up a file

## Concept

A file is always **text**. A line that looks like `42` arrives as the string
`"42\n"`, not the number 42 -- so before you can do arithmetic you must convert
it with `int()` (1.11), exactly as you did with `input()`.

`int()` is happy to ignore the surrounding whitespace, so `int("42\n")` is
`42` -- you don't even need to strip first.

```python
total = 0
with open("prices.txt") as f:
    for line in f:
        total += int(line)
```

## Example

For a `prices.txt` of:

```
10
25
7
```

the total is `42`.

## Your task

`prices.txt` holds one whole number per line. Read them, add them all up, and
print the total.

## Done when

- The program prints the sum of every number in the file.
- Negative numbers and a single-line file both work.
- You opened the file with `with` and converted each line with `int()`.
