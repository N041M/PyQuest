`re.sub(pattern, replacement, text)` nahradí každou shodu. Tvůj vzor je úsek číslic,
tvé nahrazení je `"#"`.

---

`r"\d+"` odpovídá celému úseku číslic, takže každý úsek se stane jedním `#`:
`re.sub(r"\d+", "#", text)` je celá funkce.

---

import re


def redact(text):
    return re.sub(r"\d+", "#", text)
