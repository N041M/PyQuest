Usa dois grupos de captura, um para a chave e outro para o valor, com um `=`
literal entre eles: `r"(\w+)=(\w+)"`.

---

Com dois grupos, `re.findall(pattern, text)` devolve uma lista de tuplos
`(key, value)`. `dict(...)` dessa lista é o dicionário de configuração.

---

import re


def parse_config(text):
    return dict(re.findall(r"(\w+)=(\w+)", text))
