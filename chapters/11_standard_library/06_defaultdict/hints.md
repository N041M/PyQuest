`from collections import defaultdict`, then `groups = defaultdict(list)`. The
`list` is the factory: every new key starts as an empty list.

---

Loop the words; for each, `groups[len(w)].append(w)`. The key is the length,
the value is the growing list. Return `dict(groups)` at the end.

---

from collections import defaultdict


def group_by_length(words):
    groups = defaultdict(list)
    for w in words:
        groups[len(w)].append(w)
    return dict(groups)
