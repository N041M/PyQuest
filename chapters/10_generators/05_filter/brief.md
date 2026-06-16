# 10.5 -- filter while you yield

## Concept

A generator does not have to yield on every pass. Put the `yield` behind an
`if`, and you **filter** the stream as it flows -- skipping the items you don't
want, emitting only the ones you do.

```python
def shouts(words):
    for w in words:
        if w.isupper():
            yield w          # only the all-caps words come out
```

`list(shouts(["hi", "STOP", "go", "NOW"]))` is `["STOP", "NOW"]`. The loop
visits every word; the `yield` runs only when the `if` is true.

## Example

```python
def positives(nums):
    for n in nums:
        if n > 0:
            yield n
```

`list(positives([-1, 4, 0, 2]))` is `[4, 2]`.

## Your task

Define a generator `evens(nums)` that yields only the **even** numbers of
`nums`, keeping their original order. (A number is even when `n % 2 == 0`.) If
none are even, it yields nothing.

## Done when

- `list(evens([1, 2, 3, 4]))` is `[2, 4]`.
- `list(evens([1, 3, 5]))` is `[]`; `list(evens([]))` is `[]`.
- You use `yield` behind an `if` -- not a returned list or comprehension.
