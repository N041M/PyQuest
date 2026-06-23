`date.fromisoformat(text)` promění řetězec na objekt data. Ulož ho do proměnné.

---

Přečti `d.year`, `d.month`, `d.day` z toho objektu a vrať je jako n-tici.

---

from datetime import date


def parts(text):
    d = date.fromisoformat(text)
    return (d.year, d.month, d.day)
