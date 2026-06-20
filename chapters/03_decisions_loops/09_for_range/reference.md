**`range(n)`** produces the integers `0, 1, …, n - 1` — `n` numbers starting at
zero — and a **`for`** loop runs its block once for each, binding the loop
variable to the current value.

- `range(n)` stops **before** `n` (half-open), so `range(5)` is `0,1,2,3,4` —
  five passes.
- `range(start, stop)` begins at `start`; `range(start, stop, step)` counts by
  `step` (which may be negative to count down).
- `range` is lazy — it yields numbers on demand without building a list — so a
  huge range costs nothing until iterated.

```python
for i in range(3):
    print(i)              # 0, 1, 2

for i in range(2, 6):
    print(i)              # 2, 3, 4, 5
```
