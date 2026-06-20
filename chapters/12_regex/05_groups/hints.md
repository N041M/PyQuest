Wrap each part you want in parentheses: `r"(\d+)-(\d+)-(\d+)"`. Each `(...)` is a
capture group.

---

`m = re.match(pattern, text)` then read `m.group(1)`, `m.group(2)`, `m.group(3)`.
They're strings, so wrap each in `int(...)` for the tuple.

---

import re


def parse_date(text):
    m = re.match(r"(\d+)-(\d+)-(\d+)", text)
    return (int(m.group(1)), int(m.group(2)), int(m.group(3)))
