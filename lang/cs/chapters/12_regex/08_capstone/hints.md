Použij dvě zachytávací skupiny, jednu pro klíč a jednu pro hodnotu, s doslovným `=`
mezi nimi: `r"(\w+)=(\w+)"`.

---

Se dvěma skupinami `re.findall(pattern, text)` vrátí seznam n-tic `(klíč, hodnota)`.
`dict(...)` toho seznamu je konfigurační slovník.

---

import re


def parse_config(text):
    return dict(re.findall(r"(\w+)=(\w+)", text))
