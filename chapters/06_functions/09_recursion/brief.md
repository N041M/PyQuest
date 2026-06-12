# 6.9 -- Recursion: a function calling itself

## Concept

A function may call **itself**. That is called **recursion**, and it works
whenever a problem contains a smaller copy of the same problem.

The factorial is the classic: `5!` means `5 * 4 * 3 * 2 * 1`. But look again:

> `5!` is just `5 * 4!` -- and `4!` is `4 * 3!` ...

A recursive function states exactly that, plus a **base case** -- the smallest
input answered directly, with no further calls:

```python
def fact(n):
    if n == 0:
        return 1            # base case: 0! is 1
    return n * fact(n - 1)  # the smaller copy of the same problem
```

`fact(3)` runs as `3 * fact(2)` -> `3 * 2 * fact(1)` -> `3 * 2 * 1 * fact(0)`
-> `3 * 2 * 1 * 1` = `6`. Without the base case the calls would never stop --
recursion's version of an endless loop.

You could compute a factorial with a `for` loop -- but the *lesson* here is the
self-call, so this puzzle requires it.

## Example

```python
fact(0)    # 1
fact(3)    # 6
fact(5)    # 120
```

## Your task

Define `fact(n)` that returns `n!` **recursively**: a base case for `0`, and
`n * fact(n - 1)` for the rest. `n` is never negative.

## Done when

- `fact(0)` is `1`, `fact(1)` is `1`, `fact(5)` is `120`.
- `fact` calls itself -- the checker looks for the self-call, so a loop
  version won't pass.
