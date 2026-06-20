A file object is **iterable**: looping over it yields the file **one line at a
time**, without loading the whole thing into memory. This is the standard way to
process a file line by line.

- `for line in f:` binds `line` to each line **including its trailing newline**
  `"\n"`; call `line.strip()` (or `.rstrip("\n")`) to drop it.
- It reads lazily, so it handles large files comfortably.
- `f.readlines()` instead returns a **list** of all lines at once — fine for
  small files, wasteful for big ones.

```python
with open("log.txt") as f:
    for line in f:
        print(line.strip())   # one line per pass, newline removed
```
