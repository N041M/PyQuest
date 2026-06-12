# 1.4 -- Comments

## Concept

A **comment** is a note in your code that Python ignores. Anything after a `#` on
a line is skipped when the program runs. Comments are for humans -- to explain
what the code does.

```python
# This whole line is a note and does nothing.
print("Hi")   # Text after # on a code line is also ignored.
```

Only `print("Hi")` runs above. The two notes are skipped.

A second, very practical use: **commenting out** code. If you put a `#` in front
of a line of real code, that line stops running -- without deleting it. This is
how you switch a line off temporarily.

```python
# print("off")
print("on")
```

Only `on` is printed; the first line is now a comment.

## Common misconception

Putting `#` in front of a line does **not** delete it or cause an error -- the
line is simply not run. Remove the `#` and it runs again.

## Your task

The starter file already contains a line that prints `Hidden`. **Comment it out**
so it does not run -- do **not** delete it -- and add a line that prints
`Visible`.

The program must print only:

```
Visible
```

## Done when

- The output is exactly `Visible`.
- The `print("Hidden")` line is still in the file, but commented out with a `#`
  so it does not run. (This puzzle is about *commenting out*, so deleting the
  line does not count.)
