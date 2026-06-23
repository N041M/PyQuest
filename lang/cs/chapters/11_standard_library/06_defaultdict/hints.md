`from collections import defaultdict`, pak `groups = defaultdict(list)`. `list` je
továrna: každý nový klíč začne jako prázdný seznam.

---

Procházej slova; pro každé `groups[len(w)].append(w)`. Klíč je délka, hodnota je
rostoucí seznam. Na konci vrať `dict(groups)`.

---

from collections import defaultdict


def group_by_length(words):
    groups = defaultdict(list)
    for w in words:
        groups[len(w)].append(w)
    return dict(groups)
