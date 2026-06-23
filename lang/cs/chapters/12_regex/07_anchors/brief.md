# 12.7 -- Kotvy: shoda celého řetězce

## Koncept

`re.search` je spokojený, pokud se vzor objeví **kdekoli**. Abys **validoval
formát**, potřebuješ, aby odpovídal *celý* řetězec -- žádné zbylé znaky.

Dva způsoby, jak to vyžadovat:

- **Kotvy** ve vzoru: `^` váže na **začátek**, `$` na **konec**, takže
  `r"^[A-Z]{2}\d{4}$"` musí pokrýt celý řetězec.
- **`re.fullmatch`**, který za tebe vyžaduje, aby vzor pokryl celý řetězec -- žádné
  kotvy nejsou potřeba.

```python
import re

re.fullmatch(r"[A-Z]{2}\d{4}", "AB1234")     # matches
re.fullmatch(r"[A-Z]{2}\d{4}", "AB1234x")    # None -- trailing junk
re.search(r"[A-Z]{2}\d{4}", "AB1234x")       # matches -- search ignores the x
```

Kód produktu tady jsou dvě velká písmena, pak čtyři číslice: `AB1234`.

## Příklad

```python
import re

def is_word(text):
    return re.fullmatch(r"[a-z]+", text) is not None
```

## Tvůj úkol

Pomocí **`re.fullmatch`** (nebo `^...$`) definuj `is_valid_code(text)`, která vrátí
`True` jen tehdy, když je `text` přesně **dvě velká písmena následovaná čtyřmi
číslicemi** (např. `"AB1234"`), jinak `False`.

## Hotovo, když

- `is_valid_code("AB1234")` je `True`.
- `is_valid_code("ab1234")`, `is_valid_code("AB123")`, `is_valid_code("AB1234x")`
  jsou všechny `False`.
- Odpovídá celý řetězec (fullmatch nebo kotvy), ne ručně psaná kontrola délky.
