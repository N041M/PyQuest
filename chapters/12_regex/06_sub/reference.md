**`re.sub(pattern, repl, text)`** is pattern-driven search-and-replace: it returns
a **new** string with **every** non-overlapping match of `pattern` replaced by
`repl`. Where `str.replace` swaps a fixed substring, `re.sub` swaps anything the
pattern describes.

- Because a quantified pattern matches a **run**, each run collapses to one
  replacement: `re.sub(r"\d+", "#", "a12b3")` is `"a#b#"`, not `"a##b#"`.
- No match leaves the text unchanged. An optional `count=` limits how many
  replacements are made.
- `repl` may reference captured groups with `\1`, `\2`, … (e.g.
  `re.sub(r"(\w+)@(\w+)", r"\2.\1", s)`), or be a **function** that receives each
  match and returns its replacement, for logic too complex for a template.

```python
import re

re.sub(r"\s+", " ", "too   many    spaces")   # 'too many spaces'
re.sub(r"\d+", "#", "call 555-1234")           # 'call #-#'
re.sub(r"(\d+)", r"[\1]", "x12")               # 'x[12]'
```
