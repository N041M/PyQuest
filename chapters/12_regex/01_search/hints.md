`import re`, then `re.search(pattern, text)`. The pattern for a single digit is
the raw string `r"\d"`.

---

`re.search` returns a match object when it finds the pattern, or `None` when it
doesn't. Turn that into a bool with `is not None`.

---

import re


def has_digit(text):
    return re.search(r"\d", text) is not None
