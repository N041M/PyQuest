# 14.4 -- sorted(key=lambda): sort by a derived value

## Concept

`sorted` (chapter 5) orders items by their natural order. Its **`key=`** argument
changes *what* it sorts on: a function mapping each item to the value to compare.
An inline **lambda** is the usual way to write that:

```python
words = ["pear", "fig", "apple"]
sorted(words, key=len)                  # ['fig', 'pear', 'apple']
sorted(words, key=lambda w: w[-1])      # by last letter
```

- `key` is called once per item; `sorted` then orders items by those key values.
- The lambda lets you sort by anything **derived** from an item -- its length, a
  field, a computed score -- without changing the items themselves.
- `sorted` is **stable**: items with equal keys keep their original order.

## Example

```python
def by_size(nums):
    return sorted(nums, key=lambda n: abs(n))   # by distance from zero
```

## Your task

Using **`sorted`** with a **`key=lambda`**, define `by_last(words)` that returns
the words sorted by their **last character**.

## Done when

- `by_last(["pear", "fig", "kiwi"])` returns `["fig", "kiwi", "pear"]`
  (last letters g, i, r are in order).
- `by_last([])` returns `[]`.
- The order comes from `sorted(..., key=lambda ...)`, not a manual sort.
