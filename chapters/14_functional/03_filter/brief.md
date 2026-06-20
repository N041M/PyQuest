# 14.3 -- filter: keep what passes

## Concept

Where `map` transforms every item, **`filter`** keeps only **some** of them.
You give it a **predicate** -- a function that returns true or false -- and it
keeps each item the predicate says yes to:

```python
list(filter(lambda x: x > 0, [-1, 2, -3, 4]))     # [2, 4]
```

- `filter(pred, iterable)` yields each item for which `pred(item)` is truthy,
  dropping the rest, in order.
- Like `map`, it returns a **lazy iterator**, so wrap it in `list(...)`.

(The comprehension `[x for x in items if pred(x)]` does the same; this puzzle is
about `filter` itself.)

## Example

```python
def nonempty(strings):
    return list(filter(lambda s: s != "", strings))
```

## Your task

Using **`filter`**, define `evens(nums)` that returns a list of only the even
numbers in `nums`.

## Done when

- `evens([1, 2, 3, 4])` returns `[2, 4]`.
- `evens([1, 3, 5])` returns `[]`.
- The selection is done with `filter`, not a comprehension or manual loop.
