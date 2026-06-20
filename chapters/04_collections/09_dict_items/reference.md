**`d.items()`** yields each `(key, value)` pair, so a `for` loop with two
variables walks the whole dictionary, unpacking each pair as it goes.

- `for k, v in d.items():` binds `k` to the key and `v` to its value each pass.
- `d.keys()` and `d.values()` iterate just the keys or just the values; looping
  the dict directly (`for k in d`) iterates the **keys**.
- Iteration order is the **insertion order** (the order keys were first added).

```python
prices = {"pen": 2, "ink": 5}
for item, cost in prices.items():
    print(item, cost)        # pen 2 / ink 5
```
