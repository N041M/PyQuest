Envolve cada parte que queres em parênteses: `r"(\d+)-(\d+)-(\d+)"`. Cada
`(...)` é um grupo de captura.

---

`m = re.match(pattern, text)` e depois lê `m.group(1)`, `m.group(2)`,
`m.group(3)`. São cadeias de caracteres, por isso envolve cada uma em
`int(...)` para o tuplo.

---

import re


def parse_date(text):
    m = re.match(r"(\d+)-(\d+)-(\d+)", text)
    return (int(m.group(1)), int(m.group(2)), int(m.group(3)))
