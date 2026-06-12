# 3.4 -- elif

## Concept

`elif` (short for "else if") adds **more branches** between `if` and `else`.
Python checks each condition in order and runs the **first** one that is `True`;
the rest are skipped. `else` (optional) catches everything left over.

```python
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
```

Order matters: because the first true branch wins, you usually go from the most
specific or highest condition downward.

## Example

```python
n = 0
if n < 0:
    print("negative")
elif n == 0:
    print("zero")
else:
    print("positive")
# prints: zero
```

## Your task

Read a whole number and print exactly one of:

- `negative` if it is less than 0,
- `zero` if it is 0,
- `positive` if it is greater than 0.

For input `0` the output is:

```
zero
```

## Done when

- `-3` prints `negative`, `0` prints `zero`, `5` prints `positive`.
- Exactly one line is printed for any input.
