`datetime.strptime(text, format)` parses the string. The format mirrors the
timestamp: `"%Y-%m-%d %H:%M"`.

---

The parsed object is a datetime with a `.hour` attribute. Return that.

---

from datetime import datetime


def hour_of(text):
    return datetime.strptime(text, "%Y-%m-%d %H:%M").hour
