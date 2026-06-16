# 10.7 -- stop early

## Concept

A generator ends the moment its function ends -- and a plain `return` (with no
value) inside a generator means "stop now, no more items". So a generator can
decide to **finish early**, before the input runs out.

```python
def before_blank(words):
    for w in words:
        if w == "":
            return          # stop the generator here
        yield w
```

`list(before_blank(["a", "b", "", "c"]))` is `["a", "b"]` -- once the blank is
reached, `return` ends the generator and `"c"` is never produced.

## Example

```python
def while_positive(nums):
    for n in nums:
        if n <= 0:
            return
        yield n

list(while_positive([3, 1, -1, 5]))    # [3, 1]
```

## Your task

Define a generator `until_zero(nums)` that yields each number **until it reaches
a `0`**, then stops. The `0` itself, and anything after it, is **not** yielded.
If there is no `0`, it yields the whole list.

## Done when

- `list(until_zero([1, 2, 0, 3]))` is `[1, 2]`.
- `list(until_zero([0, 9]))` is `[]`; `list(until_zero([1, 2, 3]))` is
  `[1, 2, 3]`.
- You use `yield`, and stop early when you hit a `0`.
