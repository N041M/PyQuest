A list is iterable, so **`for x in lst`** visits each item in order, binding the
loop variable to the item itself (not its index).

- This is the usual way to read a list. When you also need the position, pair it
  with `range(len(lst))` or `enumerate` (chapter 5).
- **`len(lst)`** gives the item count; **slicing** (`lst[1:3]`, `lst[::-1]`)
  works exactly as on strings and returns a new list.

```python
for name in ["Ada", "Linus"]:
    print(name)

total = 0
for n in [3, 1, 4]:
    total += n           # iterate and accumulate
```
