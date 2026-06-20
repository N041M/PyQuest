Import both `date` and `timedelta`. Parse the text, then add
`timedelta(days=n)` to the date.

---

`date.fromisoformat(text) + timedelta(days=n)` gives a new date; call
`.isoformat()` on it for the string. Negative `n` just works.

---

from datetime import date, timedelta


def add_days(text, n):
    return (date.fromisoformat(text) + timedelta(days=n)).isoformat()
