Tři kroky, tři nástroje: `datetime.strptime(timestamp, "%Y-%m-%d %H:%M")` k
parsování, `+ timedelta(hours=hours)` k posunu, `.strftime("%Y-%m-%d %H:%M")` k
formátování.

---

Naimportuj `datetime` a `timedelta`. Rozparsuj na datetime, přičti timedelta, pak
vrať strftime výsledku. Záporné hodiny fungují stejně.

---

from datetime import datetime, timedelta


def add_hours(timestamp, hours):
    dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M")
    dt = dt + timedelta(hours=hours)
    return dt.strftime("%Y-%m-%d %H:%M")
