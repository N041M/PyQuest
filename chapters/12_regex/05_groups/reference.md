Parentheses **`(...)`** in a pattern create a **capture group** — a sub-part of
the match the engine remembers so you can read it back. The match object exposes
them:

- **`m.group(n)`** returns the text the *n*-th group captured, numbered left to
  right from 1; **`m.group(0)`** (or `m.group()`) is the whole match.
- **`m.groups()`** returns every group's text as a tuple — ideal for unpacking.
- Captured text is a **string**; convert with `int(...)` as needed. A group that
  didn't participate is `None`.

So one pattern both **validates** the shape and **extracts** the fields. `re.match`
anchors at the start and returns the match object or `None`; guard for `None`
before reading groups when the input might not match. Name groups with
`(?P<name>...)` and read them via `m.group("name")` for clarity.

```python
import re

m = re.match(r"(\d+)-(\d+)-(\d+)", "2026-06-20")
m.groups()                # ('2026', '06', '20')
tuple(int(p) for p in m.groups())   # (2026, 6, 20)
```
