Nejprve řetězec rozparsuj na datum pomocí `date.fromisoformat(text)`. Objekt data
ti umí říct svůj den v týdnu.

---

`.weekday()` vrátí 0 pro pondělí až 6 pro neděli. Zavolej ho na rozparsovaném datu a
vrať výsledek.

---

from datetime import date


def weekday(text):
    return date.fromisoformat(text).weekday()
