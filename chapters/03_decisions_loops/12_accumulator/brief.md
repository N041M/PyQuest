# 3.12 -- The accumulator pattern

## Concept

A very common loop pattern: keep a **running total** in a variable, start it at
`0`, and add to it on each pass. The variable "accumulates" the result.

```python
total = 0
for n in [4, 2, 9]:
    total = total + n
print(total)        # 15
```

The key steps are: **start at 0 before the loop**, **add inside the loop**, **use
the result after the loop**. The same shape works for counting (start at 0, add 1
each time) or building a string (start at "", add a piece each time).

This puzzle combines what you have learned: a `for` loop, `range`, reading input,
and an accumulator.

## Example

```python
total = 0
for _ in range(3):
    total = total + int(input())
print(total)
```

(`_` is a normal variable name often used when you don't need the loop value.)

## Your task

Read a whole number `n` (a count). Then read `n` more whole numbers, one per
line, and print their **sum**.

For the input `3`, then `10`, `20`, `5`, the output is:

```
35
```

## Done when

- Count `3` with `10, 20, 5` prints `35`.
- A count of `0` reads no further numbers and prints `0`.
- The numbers may be negative.
