`from collections import Counter` nahoře. `Counter` udělá celé sčítání, když mu
předáš seznam.

---

`Counter(items)` už vrací počty a Counter se porovnává jako rovný prostému slovníku
stejných počtů -- takže ho můžeš vrátit přímo.

---

from collections import Counter


def tally(items):
    return Counter(items)
