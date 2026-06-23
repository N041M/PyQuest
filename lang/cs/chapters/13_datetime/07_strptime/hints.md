`datetime.strptime(text, format)` rozparsuje řetězec. Formát zrcadlí časové
razítko: `"%Y-%m-%d %H:%M"`.

---

Rozparsovaný objekt je datetime s atributem `.hour`. Ten vrať.

---

from datetime import datetime


def hour_of(text):
    return datetime.strptime(text, "%Y-%m-%d %H:%M").hour
