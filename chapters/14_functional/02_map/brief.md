# 14.2 -- map: apply to every item

## Concept

**`map(func, iterable)`** runs `func` on **every** item and yields the results.
It's the "apply to each" pattern as a higher-order function -- a function that
takes another function:

```python
list(map(str.upper, ["a", "b"]))     # ['A', 'B']
list(map(lambda x: x * x, [1, 2, 3])) # [1, 4, 9]
```

- `map` returns a **lazy iterator**, so wrap it in `list(...)` to get a list.
- The function can be a `lambda`, a `def`, or a built-in like `str.upper` or
  `int`.

(A list comprehension `[f(x) for x in items]` does the same thing and often reads
more naturally; this puzzle is about learning `map` itself, the tool you'll meet
in plenty of code.)

## Example

```python
def lengths(words):
    return list(map(len, words))
```

## Your task

Using **`map`**, define `squares(nums)` that returns a list of each number in
`nums` squared.

## Done when

- `squares([1, 2, 3])` returns `[1, 4, 9]`.
- `squares([])` returns `[]`.
- The mapping is done with `map`, not a comprehension or manual loop.
