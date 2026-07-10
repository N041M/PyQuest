`from collections import defaultdict`, depois `groups = defaultdict(list)`.
O `list` é a factory: cada chave nova começa como uma lista vazia.

---

Percorre as palavras num ciclo; para cada uma, `groups[len(w)].append(w)`.
A chave é o comprimento, o valor é a lista que vai crescendo. Devolve
`dict(groups)` no final.

---

from collections import defaultdict


def group_by_length(words):
    groups = defaultdict(list)
    for w in words:
        groups[len(w)].append(w)
    return dict(groups)
