Parse both strings into dates, then subtract them. `date_b - date_a` is a
timedelta.

---

A timedelta has a `.days` attribute. For "from a to b", subtract `a` from `b`:
`(date.fromisoformat(b) - date.fromisoformat(a)).days`.

---

from datetime import date


def days_between(a, b):
    return (date.fromisoformat(b) - date.fromisoformat(a)).days
