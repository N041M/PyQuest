# 10.1 -- yield: a function that pauses

## Concept

A normal function `return`s **once** and is done. A **generator** is a
function that uses `yield` instead: each `yield` hands back **one** value and
**pauses** the function right there. Ask for the next value and it **resumes**
from where it stopped.

```python
def two_words():
    yield "hello"
    yield "world"
```

Calling it does **not** run the body. It hands you a **generator** -- an object
you pull values from, one at a time, usually with a `for` loop:

```python
for w in two_words():
    print(w)        # hello, then world
```

The payoff: a generator produces a sequence **without building the whole list
in memory**. You will feel that in 10.3.

## Example

```python
def count_up(n):
    i = 1
    while i <= n:
        yield i
        i = i + 1
```

`list(count_up(3))` is `[1, 2, 3]` -- each loop pass yields one number, then
pauses until the next is asked for.

## Your task

Define a generator `count_down(n)` that **yields** the whole numbers from `n`
down to `1`, in that order. If `n` is `0` (or less), it yields nothing.

## Done when

- `list(count_down(5))` is `[5, 4, 3, 2, 1]`.
- `list(count_down(1))` is `[1]`; `list(count_down(0))` is `[]`.
- You use `yield` -- so calling `count_down` returns a generator, not a list.
