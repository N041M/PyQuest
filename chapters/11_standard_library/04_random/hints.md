You need three steps: copy the list, seed the generator, shuffle the copy.
`out = list(items)` makes the copy so the original is safe.

---

`random.seed(seed)` fixes the starting point; `random.shuffle(out)` reorders
`out` in place (it returns None, so don't `return random.shuffle(...)`). Return
`out` afterwards.

---

import random


def shuffled(items, seed):
    out = list(items)
    random.seed(seed)
    random.shuffle(out)
    return out
