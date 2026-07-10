`import re`, depois `re.findall(pattern, text)` devolve uma lista de todas as
correspondências. Queres sequências de dígitos.

---

O padrão `r"\d+"` corresponde a um ou mais dígitos seguidos, por isso cada
correspondência é um número completo. `re.findall(r"\d+", text)` é a resposta
inteira.

---

import re


def all_numbers(text):
    return re.findall(r"\d+", text)
