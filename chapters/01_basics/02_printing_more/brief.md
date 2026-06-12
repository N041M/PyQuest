# 1.2 -- Printing more

## Concept

Two new ideas, both about `print`.

**1. Many prints run in order.** Each `print(...)` puts its text on its own line,
and Python runs them top to bottom. Three `print` lines make three output lines.

**2. One print can show several values.** Put several things inside the
parentheses separated by **commas**, and `print` shows them on one line with a
single space between each:

```python
print("a", "b", "c")
```

shows:

```
a b c
```

You can mix text and numbers this way. Numbers do **not** need quotes; text does.

## Example

```python
print("Scores:")
print(10, 20, 30)
```

shows:

```
Scores:
10 20 30
```

The first line is one print; the second print has three values separated by
commas, so they share a line with spaces between them.

## Your task

Produce exactly these two lines:

```
Counting:
1 2 3
```

Use two `print` statements: the first prints the word, the second prints the
three numbers `1`, `2`, `3` as separate values (let `print` add the spaces).

## Done when

- The output is exactly two lines: `Counting:` then `1 2 3`.
- The second line comes from numbers separated by commas, not from typing the
  text `"1 2 3"` yourself.
