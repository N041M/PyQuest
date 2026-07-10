`datetime.strptime(text, format)` analisa a cadeia. O formato reflete a marca
temporal: `"%Y-%m-%d %H:%M"`.

---

O objeto analisado é um datetime com um atributo `.hour`. Devolve-o.

---

from datetime import datetime


def hour_of(text):
    return datetime.strptime(text, "%Y-%m-%d %H:%M").hour
