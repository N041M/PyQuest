Precisas de três passos: copiar a lista, definir a seed do gerador, baralhar
a cópia. `out = list(items)` faz a cópia para que o original fique seguro.

---

`random.seed(seed)` fixa o ponto de partida; `random.shuffle(out)` reordena
`out` no próprio local (devolve None, por isso não faças `return
random.shuffle(...)`). Devolve `out` a seguir.

---

import random


def shuffled(items, seed):
    out = list(items)
    random.seed(seed)
    random.shuffle(out)
    return out
