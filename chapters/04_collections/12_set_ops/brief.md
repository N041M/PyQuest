# 4.12 -- Combining sets

## Concept

Sets can be combined like in maths:

- **intersection** `a & b` -- items in **both**
- **union** `a | b` -- items in **either**
- **difference** `a - b` -- items in `a` but not `b`

```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)    # {2, 3}
print(a | b)    # {1, 2, 3, 4}
print(a - b)    # {1}
```

These answer questions like "which items do two groups share?" without writing a
loop. (`a.intersection(b)` and `a.union(b)` do the same as `&` and `|`.)

## Example

```python
x = {"a", "b"}
y = {"b", "c"}
print(len(x & y))   # 1   (just "b")
```

## Your task

Read a first group: a count `n`, then `n` words. Then a second group: a count
`m`, then `m` words. Print **how many distinct words appear in both** groups.

For first group `a`, `b` and second group `b`, `c`:

```
1
```

(Only `b` is in both.)

## Done when

- `{a, b}` and `{b, c}` print `1`.
- Empty groups give `0`; duplicates within a group count once.
