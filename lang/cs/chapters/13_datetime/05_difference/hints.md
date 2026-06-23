Rozparsuj oba řetězce na data, pak je odečti. `date_b - date_a` je timedelta.

---

timedelta má atribut `.days`. Pro „od a do b“ odečti `a` od `b`:
`(date.fromisoformat(b) - date.fromisoformat(a)).days`.

---

from datetime import date


def days_between(a, b):
    return (date.fromisoformat(b) - date.fromisoformat(a)).days
