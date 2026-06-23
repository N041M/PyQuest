# 12.5 -- Skupiny: zachyť části

## Koncept

Závorky **`(...)`** ve vzoru vyznačují **zachytávací skupinu**: kousek shody, který
chceš vytáhnout. Objekt shody ti pak každý vrátí:

```python
import re

m = re.match(r"(\d+)-(\d+)-(\d+)", "2026-06-20")
m.group(1)     # '2026'
m.group(2)     # '06'
m.groups()     # ('2026', '06', '20')
```

- `re.match` odpovídá od **začátku** řetězce a vrací objekt shody (nebo `None`).
- `m.group(n)` vrátí text, který zachytila *n*-tá skupina (`group(0)` je celá
  shoda); `m.groups()` vrátí je všechny jako n-tici.
- Zachycený text je stále řetězec -- `int(m.group(1))`, pokud chceš číslo.

Jeden vzor tedy zároveň kontroluje tvar i extrahuje pole.

## Příklad

```python
import re

def split_pair(text):
    m = re.match(r"(\w+):(\w+)", text)
    return (m.group(1), m.group(2))
```

## Tvůj úkol

Pomocí **`re.match`** se zachytávacími skupinami definuj `parse_date(text)`, která
bere datum jako `"2026-06-20"` a vrátí n-tici **celých čísel** `(year, month, day)`.

## Hotovo, když

- `parse_date("2026-06-20")` vrátí `(2026, 6, 20)`.
- `parse_date("1999-01-05")` vrátí `(1999, 1, 5)`.
- Pole pocházejí ze zachytávacích skupin, ne z `text.split("-")`.
