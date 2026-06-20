The pattern for the code is `r"[A-Z]{2}\d{4}"` -- two uppercase letters, then
four digits. The trick is making the WHOLE string match it.

---

`re.fullmatch(pattern, text)` requires the pattern to cover the entire string, so
trailing characters fail. Return whether it found a match with `is not None`.

---

import re


def is_valid_code(text):
    return re.fullmatch(r"[A-Z]{2}\d{4}", text) is not None
