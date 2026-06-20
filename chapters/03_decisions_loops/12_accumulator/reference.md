The **accumulator** pattern builds up a result across a loop. You initialise a
variable **before** the loop, then update it on **every** pass; after the loop it
holds the combined result.

- For a sum, start the total at `0` and add each value (`total = total + x`, or
  `total += x`). Starting at `0` is the identity for `+`, so an empty loop
  leaves it `0`.
- The same shape counts (start at 0, `+= 1` per match), builds a string (start
  `""`, `+=`), or collects a list (start `[]`, `.append`).
- The accumulator must live **outside** the loop — declaring it inside would
  reset it every pass.

```python
total = 0
for n in [3, 1, 4]:
    total += n            # 3, then 4, then 8
print(total)             # 8
```
