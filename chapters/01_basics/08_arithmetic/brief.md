# 1.8 -- Arithmetic and order

## Concept

Python does math with these signs (called **operators**):

- `+` add
- `-` subtract
- `*` multiply
- `/` divide

```python
print(2 + 3)   # 5
print(10 - 4)  # 6
print(6 * 7)   # 42
```

**Order matters.** Just like in school maths, `*` and `/` happen **before**
`+` and `-`. So:

```python
print(2 + 3 * 4)   # 14, not 20  -- 3*4 first, then +2
```

To force a different order, wrap a part in **parentheses** `( )`. Whatever is
inside parentheses is worked out first:

```python
print((2 + 3) * 4)   # 20  -- 2+3 first, then *4
```

This is the single most common source of "wrong number" bugs, so it is worth
getting comfortable with now.

## Example

```python
print(1 + 2 * 3)     # 7
print((1 + 2) * 3)   # 9
```

## Your task

Print these two lines:

```
14
20
```

- The first line is `2 + 3 * 4` with no parentheses (multiplication first).
- The second line is the same numbers but with parentheses so the addition
  happens first: `(2 + 3) * 4`.

## Done when

- Output is `14` then `20`.
- The difference between the lines comes only from parentheses changing the
  order.
