# 4.7 -- Tuples and unpacking

## Concept

A **tuple** is like a list, but **immutable** -- once made, it can't be changed.
You write one with parentheses (or just commas):

```python
point = (3, 7)
print(point[0])    # 3
```

**Unpacking** assigns several variables at once from a tuple (or list):

```python
x, y = point       # x = 3, y = 7
```

The left side names match the items on the right, in order. A neat trick this
enables is **swapping** two variables without a temporary:

```python
a, b = 1, 2
a, b = b, a        # now a = 2, b = 1
```

The right-hand side `b, a` builds a tuple, which is then unpacked into `a, b`.

## Example

```python
a, b = 10, 20
a, b = b, a
print(a)    # 20
print(b)    # 10
```

## Your task

Read two whole numbers (each on its own line). **Swap** them using tuple
unpacking, then print the first, then the second.

For input `3` then `7`:

```
7
3
```

## Done when

- `3, 7` prints `7` then `3`.
- It works for any two numbers (including two equal ones).
