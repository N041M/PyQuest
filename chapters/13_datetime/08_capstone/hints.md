Three steps, three tools: `datetime.strptime(timestamp, "%Y-%m-%d %H:%M")` to
parse, `+ timedelta(hours=hours)` to shift, `.strftime("%Y-%m-%d %H:%M")` to
format.

---

Import `datetime` and `timedelta`. Parse into a datetime, add the timedelta, then
return the strftime of the result. Negative hours work the same way.

---

from datetime import datetime, timedelta


def add_hours(timestamp, hours):
    dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M")
    dt = dt + timedelta(hours=hours)
    return dt.strftime("%Y-%m-%d %H:%M")
