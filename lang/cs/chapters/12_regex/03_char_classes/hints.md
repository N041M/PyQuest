Znaková třída v hranatých závorkách odpovídá jednomu z uvedených znaků. Pro
samohlásky je to `r"[aeiou]"`.

---

`re.findall(r"[aeiou]", text)` dá seznam každé nalezené samohlásky; `len(...)` toho
seznamu je počet.

---

import re


def count_vowels(text):
    return len(re.findall(r"[aeiou]", text))
