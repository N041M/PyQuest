# 12.6 -- re.sub: find and replace by pattern

## Concept

`str.replace` swaps a fixed substring. **`re.sub`** swaps everything matching a
**pattern**:

```python
import re

re.sub(r"\d+", "#", "call 555-1234 now")     # 'call #-# now'
```

- `re.sub(pattern, replacement, text)` returns a **new** string with **every**
  match of `pattern` replaced by `replacement`.
- Because `\d+` matches a whole run of digits, each run collapses to a single
  `#` -- one replacement per match, not per character.
- No match leaves the text unchanged. The replacement can also reference captured
  groups (`\1`), but a plain string is the common case.

## Example

```python
import re

def squash_spaces(text):
    return re.sub(r"\s+", " ", text)
```

## Your task

Using **`re.sub`**, define `redact(text)` that replaces every run of digits in
`text` with a single `"#"`.

## Done when

- `redact("call 555-1234")` returns `"call #-#"`.
- `redact("no digits")` returns `"no digits"`.
- Each digit *run* becomes one `#` (use `\d+`), via `re.sub` -- not a character
  loop.
