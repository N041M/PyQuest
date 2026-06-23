Slovo je jedno či více písmen v řadě. Znaková třída `[A-Za-z]` odpovídá jednomu
písmenu; kvantifikátor `+` ji přiměje odpovídat úseku.

---

`re.findall(r"[A-Za-z]+", text)` vrátí každé slovo a každou shodu zastaví u prvního
nepísmene. To je celá funkce.

---

import re


def find_words(text):
    return re.findall(r"[A-Za-z]+", text)
