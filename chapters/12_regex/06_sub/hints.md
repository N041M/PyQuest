`re.sub(pattern, replacement, text)` replaces every match. Your pattern is a run
of digits, your replacement is `"#"`.

---

`r"\d+"` matches a whole run of digits, so each run becomes one `#`:
`re.sub(r"\d+", "#", text)` is the entire function.

---

import re


def redact(text):
    return re.sub(r"\d+", "#", text)
