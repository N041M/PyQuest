# 3.9 -- for and range

## Concept

A **`for` loop** runs its block once for each item in a sequence. Combined with
**`range`**, it is the usual way to repeat something a set number of times.

`range(n)` produces the numbers `0, 1, 2, ..., n-1` (it stops *before* `n`):

```python
for i in range(4):
    print(i)
# prints 0, 1, 2, 3
```

Each time round, the loop variable (`i` here) takes the next value. You do not
manage a counter yourself -- `range` does it for you, so there is no endless-loop
risk.

`range` can also take a start and step: `range(1, 5)` is `1,2,3,4`;
`range(0, 10, 2)` is `0,2,4,6,8`.

## Example

```python
for i in range(3):
    print(i)
# prints 0, 1, 2
```

## Your task

Read a whole number `n`, then print every number from `0` up to `n-1`, each on
its own line, using a `for` loop with `range`.

For input `4` the output is:

```
0
1
2
3
```

## Done when

- `4` prints `0,1,2,3` (each on a line). `1` prints just `0`.
- `0` prints nothing.
