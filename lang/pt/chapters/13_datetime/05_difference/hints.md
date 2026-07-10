Analisa as duas cadeias para datas e depois subtrai-as. `date_b - date_a` é
um timedelta.

---

Um timedelta tem um atributo `.days`. Para "de a até b", subtrai `a` de `b`:
`(date.fromisoformat(b) - date.fromisoformat(a)).days`.

---

from datetime import date


def days_between(a, b):
    return (date.fromisoformat(b) - date.fromisoformat(a)).days
