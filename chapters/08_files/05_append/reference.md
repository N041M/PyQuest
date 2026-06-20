Mode **`"a"`** opens a file for **appending**: writes go to the **end**, and any
existing contents are kept. It's the non-destructive counterpart to `"w"`.

- `"a"` creates the file if it doesn't exist; if it does, `f.write` adds after
  what's already there — nothing is overwritten.
- `"w"` empties the file first; reach for `"a"` to grow a log or accumulate
  results across runs.
- As with `"w"`, newlines are not added for you.

```python
with open("log.txt", "a") as f:
    f.write("another entry\n")   # added at the end, old lines kept
```
