`date.fromisoformat(text)` turns the string into a date object. Store it in a
variable.

---

Read `d.year`, `d.month`, `d.day` off that object and return them as a tuple.

---

from datetime import date


def parts(text):
    d = date.fromisoformat(text)
    return (d.year, d.month, d.day)
