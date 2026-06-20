A slice takes a third part, the **step**: `s[start:stop:step]` takes every
`step`-th character. The default step is 1.

- `s[::2]` takes every second character (indexes 0, 2, 4, …).
- A **negative** step walks backwards. `s[::-1]` is the idiomatic way to
  **reverse** a string; with a negative step the default start/stop flip to the
  end and the beginning.
- `s[::-2]` takes every second character, from the end toward the start.

```python
s = "Python"
s[::2]    # 'Pto'
s[::-1]   # 'nohtyP'  -- reversed
```
