# 12.7 -- Anchors: match the whole string

## Concept

`re.search` is happy if the pattern appears **anywhere**. To **validate a
format**, you need the *entire* string to match -- no leftover characters.

Two ways to demand that:

- **Anchors** in the pattern: `^` ties to the **start**, `$` to the **end**, so
  `r"^[A-Z]{2}\d{4}$"` must span the whole string.
- **`re.fullmatch`**, which requires the pattern to cover the whole string for
  you -- no anchors needed.

```python
import re

re.fullmatch(r"[A-Z]{2}\d{4}", "AB1234")     # matches
re.fullmatch(r"[A-Z]{2}\d{4}", "AB1234x")    # None -- trailing junk
re.search(r"[A-Z]{2}\d{4}", "AB1234x")       # matches -- search ignores the x
```

A product code here is two uppercase letters then four digits: `AB1234`.

## Example

```python
import re

def is_word(text):
    return re.fullmatch(r"[a-z]+", text) is not None
```

## Your task

Using **`re.fullmatch`** (or `^...$`), define `is_valid_code(text)` that returns
`True` only when `text` is exactly **two uppercase letters followed by four
digits** (e.g. `"AB1234"`), `False` otherwise.

## Done when

- `is_valid_code("AB1234")` is `True`.
- `is_valid_code("ab1234")`, `is_valid_code("AB123")`, `is_valid_code("AB1234x")`
  are all `False`.
- The whole string is matched (fullmatch or anchors), not a hand-written length
  check.
