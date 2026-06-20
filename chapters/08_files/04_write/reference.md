Opening with mode **`"w"`** opens a file for **writing**. It **creates** the file
if absent and **truncates** it (empties it) if it already exists, so existing
contents are lost.

- **`f.write(text)`** writes a string and, unlike `print`, adds **no** trailing
  newline — include `"\n"` yourself where you want line breaks.
- `f.write` takes strings only; convert numbers with `str()` or an f-string
  first.
- Use `with` so the data is flushed and the file closed properly.

```python
with open("out.txt", "w") as f:
    f.write("first line\n")
    f.write("second line\n")   # newlines are explicit
```
