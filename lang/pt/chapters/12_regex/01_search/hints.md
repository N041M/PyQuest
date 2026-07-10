`import re`, depois `re.search(pattern, text)`. O padrão para um único dígito é
a cadeia de caracteres em bruto `r"\d"`.

---

`re.search` devolve um objeto de correspondência quando encontra o padrão, ou
`None` quando não encontra. Transforma isso num booleano com `is not None`.

---

import re


def has_digit(text):
    return re.search(r"\d", text) is not None
