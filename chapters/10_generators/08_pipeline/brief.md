# 10.8 -- Capstone: a streaming pipeline

## Concept

Nothing new -- this capstone is the chapter in miniature. The real reason
generators matter is that they **compose**: one generator's output is another
generator's input, so data flows through a **pipeline**, one item at a time,
without ever building the full list in between.

A pipeline stage is just a generator that loops over `stream` (any iterable --
a list, or *another generator*) and yields as it goes:

```python
def only_long(stream):
    for word in stream:
        if len(word) >= 4:
            yield word
```

You will build a source, a filter, and a relabel stage, then wire them
together.

## Example

```python
numbers(4)                              # yields 0, 1, 2, 3
keep_even(numbers(4))                   # yields 0, 2
labelled(keep_even(numbers(4)))         # yields "#0", "#2"
```

## Your task

Define **three** generators:

- `numbers(n)` -- yields `0, 1, ..., n-1` (the source). `n <= 0` yields nothing.
- `keep_even(stream)` -- yields only the even numbers from `stream` (any
  iterable).
- `labelled(stream)` -- yields the string `"#x"` for each `x` in `stream`
  (e.g. `7` becomes `"#7"`).

Each must use `yield`. `keep_even` and `labelled` must work on **any** stream,
including the output of another generator, so they compose.

## Done when

- `list(numbers(4))` is `[0, 1, 2, 3]`; `list(numbers(0))` is `[]`.
- `list(keep_even([1, 2, 3, 4]))` is `[2, 4]`.
- `list(labelled([0, 2]))` is `["#0", "#2"]`.
- `list(labelled(keep_even(numbers(6))))` is `["#0", "#2", "#4"]`.
- All three use `yield`, and the filter/relabel stages accept any iterable.
