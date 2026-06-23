Závorky **`(...)`** ve vzoru vytvoří **zachytávací skupinu** — podčást shody, kterou
si engine zapamatuje, abys ji mohl přečíst zpět. Objekt shody je zpřístupní:

- **`m.group(n)`** vrátí text, který zachytila *n*-tá skupina, číslovaná zleva doprava
  od 1; **`m.group(0)`** (nebo `m.group()`) je celá shoda.
- **`m.groups()`** vrátí text každé skupiny jako n-tici — ideální k rozbalení.
- Zachycený text je **řetězec**; podle potřeby převeď pomocí `int(...)`. Skupina,
  která se nezúčastnila, je `None`.

Takže jeden vzor zároveň **validuje** tvar i **extrahuje** pole. `re.match` se ukotví
na začátku a vrátí objekt shody nebo `None`; než budeš číst skupiny, ošetři `None`,
když vstup nemusí sednout. Skupiny pojmenuj pomocí `(?P<name>...)` a čti je přes
`m.group("name")` pro přehlednost.

```python
import re

m = re.match(r"(\d+)-(\d+)-(\d+)", "2026-06-20")
m.groups()                # ('2026', '06', '20')
tuple(int(p) for p in m.groups())   # (2026, 6, 20)
```
