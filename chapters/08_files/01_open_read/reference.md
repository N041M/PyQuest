**`open(name)`** connects to a file on disk; the **`with`** statement manages it
so the file is **closed automatically** when the block ends, even if an error
occurs. Inside the block, the file object `f` provides the contents.

- `with open(name) as f:` opens for **reading** text (the default mode `"r"`) and
  binds the open file to `f`.
- **`f.read()`** returns the entire contents as one string. (`f.read(n)` reads at
  most `n` characters.)
- Opening a path that doesn't exist raises `FileNotFoundError`. Always use `with`
  rather than a bare `open` — it guarantees the close.

```python
with open("notes.txt") as f:
    text = f.read()      # whole file as a string
# file is closed here
```
