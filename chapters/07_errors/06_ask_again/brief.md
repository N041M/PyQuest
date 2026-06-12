# 7.6 -- Ask again: the retry loop

## Concept

The classic use of `try`/`except` in a real program: **keep asking until the
input makes sense.** Combine a `while True` loop (3.7), `break` (3.11), and
the `except` from 7.1:

```python
while True:
    try:
        n = int(input())
        break              # got a good one -- leave the loop
    except ValueError:
        pass               # bad line -- silently go around again
```

The shape to internalise:

- the **happy path** ends in `break`;
- the **except** absorbs the failure and lets the loop retry;
- after the loop, `n` is guaranteed valid -- the code below can trust it.

(`pass` is Python's "do nothing" statement -- the except block must contain
*something*.)

## Example

For the input lines `cat`, `dog`, `21` the program ignores the first two and
prints `42`.

## Your task

Read lines until one converts to a whole number, then print that number
**doubled**. Bad lines produce no output at all.

## Done when

- `21` as the first line prints `42`.
- `cat`, `dog`, `21` also prints just `42` -- the garbage is silently retried.
- Negative numbers work.
- You used a loop and `try`/`except`.
