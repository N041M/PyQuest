# 3.7 -- while

## Concept

A **`while` loop** repeats a block **as long as** a condition stays `True`. It
checks the condition, runs the block, then checks again -- over and over:

```python
count = 1
while count <= 3:
    print(count)
    count = count + 1   # move toward making the condition False
# prints 1, 2, 3
```

The line `count = count + 1` is essential: it changes `count` so the condition
will eventually become `False`. Without it the loop never stops.

## Common misconception -- the endless loop

If the condition never becomes `False`, the loop runs forever. Always make sure
something inside the loop moves toward the stopping point. (If your program seems
to hang, that is usually an endless loop.)

## Example

```python
n = 4
i = 1
while i <= n:
    print(i)
    i = i + 1
# prints 1, 2, 3, 4
```

## Your task

Read a whole number `n`, then print every number from `1` up to `n`, each on its
own line, using a `while` loop.

For input `3` the output is:

```
1
2
3
```

## Done when

- `3` prints `1`, `2`, `3`. `1` prints just `1`.
- `0` (or a negative) prints nothing -- the loop body never runs.
