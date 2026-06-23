Rozparsuj datum pomocí `date.fromisoformat(text)`, pak na něm zavolej
`.strftime(...)` s rozvržením, které chceš.

---

Formátovací řetězec pro DD/MM/YYYY je `"%d/%m/%Y"`. Lomítka se kopírují doslovně;
kódy doplní čísla s nulami.

---

from datetime import date


def pretty(text):
    return date.fromisoformat(text).strftime("%d/%m/%Y")
