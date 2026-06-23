`import re`, pak `re.search(pattern, text)`. Vzor pro jedinou číslici je surový
řetězec `r"\d"`.

---

`re.search` vrátí objekt shody, když vzor najde, nebo `None`, když ne. Proměň to na
bool pomocí `is not None`.

---

import re


def has_digit(text):
    return re.search(r"\d", text) is not None
