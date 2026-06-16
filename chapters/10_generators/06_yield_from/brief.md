# 10.6 -- yield from: pass a whole stream along

## Concept

When you want a generator to re-emit **every** item of another iterable, you
could loop and yield each one:

```python
def both(a, b):
    for x in a:
        yield x
    for y in b:
        yield y
```

Python has a shorthand for exactly that inner loop: **`yield from`**.

```python
def both(a, b):
    yield from a        # yield every item of a, one by one
    yield from b        # then every item of b
```

`yield from iterable` is "yield each value this iterable produces". The two
versions above behave identically; `yield from` just says it in one line.

## Example

```python
def repeat_each(items):
    for x in items:
        yield from (x, x)      # yield x, then x again

list(repeat_each([1, 2]))      # [1, 1, 2, 2]
```

## Your task

Define a generator `chain(a, b)` that yields **all** the items of `a`, then
**all** the items of `b`, in order. Use `yield from`. Either list may be empty.

## Done when

- `list(chain([1, 2], [3, 4]))` is `[1, 2, 3, 4]`.
- `list(chain([], [9]))` is `[9]`; `list(chain([], []))` is `[]`.
- You use `yield from`, so calling `chain` returns a generator.
