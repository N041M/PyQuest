`re.sub(pattern, replacement, text)` substitui todas as correspondências. O
teu padrão é uma sequência de dígitos, a tua substituição é `"#"`.

---

`r"\d+"` corresponde a uma sequência inteira de dígitos, por isso cada
sequência torna-se um `#`: `re.sub(r"\d+", "#", text)` é a função inteira.

---

import re


def redact(text):
    return re.sub(r"\d+", "#", text)
