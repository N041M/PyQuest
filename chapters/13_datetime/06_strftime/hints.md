Parse the date with `date.fromisoformat(text)`, then call `.strftime(...)` on it
with the layout you want.

---

The format string for DD/MM/YYYY is `"%d/%m/%Y"`. The slashes are copied through
literally; the codes fill in the padded numbers.

---

from datetime import date


def pretty(text):
    return date.fromisoformat(text).strftime("%d/%m/%Y")
