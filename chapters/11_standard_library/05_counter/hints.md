`from collections import Counter` at the top. `Counter` does the whole tally when
you hand it the list.

---

`Counter(items)` already returns the counts, and a Counter compares equal to the
plain dict of the same counts -- so you can return it directly.

---

from collections import Counter


def tally(items):
    return Counter(items)
