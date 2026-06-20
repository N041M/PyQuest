**`filter(pred, iterable)`** keeps the items for which the **predicate** `pred`
(a function returning true or false) is truthy, dropping the rest — the "keep if"
counterpart to `map`'s "transform each".

- It returns a **lazy iterator** in original order; wrap it in `list(...)` to
  collect.
- `pred` is any callable returning a truthy/falsy value — a `lambda`, a `def`, or
  a built-in. Passing **`None`** as the predicate (`filter(None, items)`) keeps
  the items that are themselves truthy, dropping `0`, `""`, `None`, etc.
- The comprehension `[x for x in items if pred(x)]` is the equivalent and often
  reads better; `filter` is the functional form.

```python
list(filter(lambda x: x > 0, [-1, 2, -3, 4]))   # [2, 4]
list(filter(None, [0, 1, "", "a", None]))        # [1, 'a']
list(filter(str.isalpha, "a1b2"))                # ['a', 'b']
```
