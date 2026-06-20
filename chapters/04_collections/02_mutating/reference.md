Lists are **mutable**: their contents can change in place, unlike strings.

- **`lst[i] = x`** replaces the item at index `i`. The index must already exist
  (assigning past the end raises `IndexError`).
- **`.pop()`** removes and **returns** the last item, shrinking the list;
  `.pop(i)` removes the item at index `i`. Popping from an empty list raises.
- Other in-place changes: `.insert(i, x)`, `.remove(value)`, `del lst[i]`.

Because the change is in place, every name referring to the same list object sees
it.

```python
lst = [10, 20, 30]
lst[1] = 99      # [10, 99, 30]
last = lst.pop() # last == 30, lst == [10, 99]
```
