Parse the string into a date first with `date.fromisoformat(text)`. A date object
can tell you its weekday.

---

`.weekday()` returns 0 for Monday through 6 for Sunday. Call it on the parsed
date and return the result.

---

from datetime import date


def weekday(text):
    return date.fromisoformat(text).weekday()
