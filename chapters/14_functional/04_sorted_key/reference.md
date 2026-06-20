`sorted`'s **`key=`** argument is a function mapping each item to the value to
sort on, so you can order by something **derived** from the items rather than the
items themselves. An inline **`lambda`** is the idiomatic way to write that key.

- `key` is called **once per item**; `sorted` orders the items by the resulting
  key values, but returns the original items. `sorted(words, key=len)` orders by
  length, `sorted(words, key=lambda w: w[-1])` by last letter.
- `sorted` is **stable**: items with equal keys keep their input order.
- Pair `key=` with **`reverse=True`** to sort descending. The same `key=` works on
  `list.sort`, `min`, and `max`.

```python
sorted(["pear", "fig", "apple"], key=len)            # ['fig', 'pear', 'apple']
sorted([-3, 1, -2], key=lambda n: abs(n))            # [1, -2, -3]
sorted(records, key=lambda r: r[1], reverse=True)    # by 2nd field, high first
```
