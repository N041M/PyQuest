Uma classe de caracteres entre parênteses retos corresponde a um dos
caracteres listados. Para vogais, isso é `r"[aeiou]"`.

---

`re.findall(r"[aeiou]", text)` dá uma lista de todas as vogais encontradas;
`len(...)` dessa lista é a contagem.

---

import re


def count_vowels(text):
    return len(re.findall(r"[aeiou]", text))
