`from datetime import date`, then `date(y, m, d)` makes the object. It has an
`.isoformat()` method that returns the YYYY-MM-DD string.

---

Chain them: `date(y, m, d).isoformat()`. The zero-padding is handled for you.

---

from datetime import date


def iso(y, m, d):
    return date(y, m, d).isoformat()
