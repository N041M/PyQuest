Naimportuj `date` i `timedelta`. Rozparsuj text, pak k datu přičti
`timedelta(days=n)`.

---

`date.fromisoformat(text) + timedelta(days=n)` dá nové datum; zavolej na něm
`.isoformat()` pro řetězec. Záporné `n` prostě funguje.

---

from datetime import date, timedelta


def add_days(text, n):
    return (date.fromisoformat(text) + timedelta(days=n)).isoformat()
