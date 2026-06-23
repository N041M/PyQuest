Obal každou část, kterou chceš, do závorek: `r"(\d+)-(\d+)-(\d+)"`. Každé `(...)` je
zachytávací skupina.

---

`m = re.match(pattern, text)` pak čti `m.group(1)`, `m.group(2)`, `m.group(3)`. Jsou
to řetězce, takže každý obal do `int(...)` pro n-tici.

---

import re


def parse_date(text):
    m = re.match(r"(\d+)-(\d+)-(\d+)", text)
    return (int(m.group(1)), int(m.group(2)), int(m.group(3)))
