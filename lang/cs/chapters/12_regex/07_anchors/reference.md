Ve výchozím stavu může vzor odpovídat **kdekoli** v řetězci. Validovat *formát*
znamená, že musí vyhovět **celý** řetězec — žádné zbylé znaky. Dva způsoby, jak to
vyžadovat:

- **Kotvy** ve vzoru: **`^`** odpovídá začátku řetězce, **`$`** konci.
  `r"^[A-Z]{2}\d{4}$"` musí pokrýt celý vstup.
- **`re.fullmatch(pattern, text)`** za tebe vyžaduje, aby vzor pokryl celý řetězec —
  žádné kotvy nejsou potřeba. Vrátí objekt shody nebo `None`.

Kontrast: `re.search(r"[A-Z]{2}\d{4}", "AB1234x")` **odpovídá** (vzor se vyskytuje),
ale `re.fullmatch(r"[A-Z]{2}\d{4}", "AB1234x")` je **`None`** (`x` zbylo). Použij
`search`/`findall` k *hledání* podřetězců, `fullmatch`/kotvy k *validaci* celé
hodnoty.

```python
import re

bool(re.fullmatch(r"[A-Z]{2}\d{4}", "AB1234"))    # True
bool(re.fullmatch(r"[A-Z]{2}\d{4}", "AB1234x"))   # False
bool(re.match(r"^\d{5}$", "12345"))               # True -- anchored form
```
