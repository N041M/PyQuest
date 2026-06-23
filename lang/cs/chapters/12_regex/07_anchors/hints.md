Vzor pro kód je `r"[A-Z]{2}\d{4}"` -- dvě velká písmena, pak čtyři číslice. Trik je
přimět CELÝ řetězec, aby mu odpovídal.

---

`re.fullmatch(pattern, text)` vyžaduje, aby vzor pokryl celý řetězec, takže koncové
znaky selžou. Vrať, zda našel shodu, pomocí `is not None`.

---

import re


def is_valid_code(text):
    return re.fullmatch(r"[A-Z]{2}\d{4}", text) is not None
