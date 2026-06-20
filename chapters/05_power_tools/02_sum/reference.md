**`sum(numbers)`** adds up an iterable of numbers and returns the total — the
accumulator loop of 3.12 as one built-in call.

- It works on any iterable of numbers (list, tuple, range, generator). `sum([])`
  is `0`.
- An optional second argument is the **start** value: `sum(nums, 100)` begins the
  total at 100.
- It only adds numbers; to total something derived from each item, feed it a
  comprehension or generator, e.g. `sum(len(w) for w in words)`.

```python
sum([3, 1, 4])              # 8
sum(range(1, 101))          # 5050
sum(len(w) for w in words)  # total characters
```
