Potřebuješ tři kroky: zkopíruj seznam, semínkuj generátor, zamíchej kopii.
`out = list(items)` udělá kopii, aby byl originál v bezpečí.

---

`random.seed(seed)` zafixuje výchozí bod; `random.shuffle(out)` přeuspořádá `out`
na místě (vrací None, takže nepiš `return random.shuffle(...)`). Poté vrať `out`.

---

import random


def shuffled(items, seed):
    out = list(items)
    random.seed(seed)
    random.shuffle(out)
    return out
