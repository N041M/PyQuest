# 10.2 -- yield inside a loop

## Concept

The real power of `yield` shows when it sits **inside a loop**: one `yield` line
runs once per pass, streaming a whole transformed sequence -- a value at a time,
never the whole list at once.

```python
def letters(word):
    for ch in word:
        yield ch.upper()
```

`list(letters("hi"))` is `["H", "I"]`. The loop walks the input; the `yield`
emits one transformed item each time round, pausing in between.

## Example

```python
def doubles(nums):
    for x in nums:
        yield x * 2
```

`list(doubles([1, 5, 9]))` is `[2, 10, 18]`.

## Your task

Define a generator `squares(n)` that **yields** the squares of the whole
numbers from `0` up to (but not including) `n`: `0, 1, 4, 9, ...`. If `n` is `0`
(or less), it yields nothing.

## Done when

- `list(squares(4))` is `[0, 1, 4, 9]`.
- `list(squares(1))` is `[0]`; `list(squares(0))` is `[]`.
- You use `yield` inside a loop -- not a returned list or comprehension.
