`from collections import Counter` no topo. O `Counter` faz toda a contagem
quando lhe entregas a lista.

---

`Counter(items)` já devolve as contagens, e um Counter é igual, na
comparação, ao dict simples com as mesmas contagens -- por isso podes
devolvê-lo diretamente.

---

from collections import Counter


def tally(items):
    return Counter(items)
