**Kvantifikátor** řídí, kolikrát se opakuje vzor bezprostředně před ním:

- **`+`** jednou nebo víckrát, **`*`** nulakrát nebo víckrát, **`?`** nula nebo jedna
  (volitelné),
- **`{n}`** přesně *n*, **`{n,m}`** mezi *n* a *m*, **`{n,}`** alespoň *n*.

`[A-Za-z]+` tedy odpovídá celému **slovu** — úseku jednoho či více písmen — a zastaví
se u prvního znaku, který nesedí, čímž tokenizuješ text a ignoruješ mezery a
interpunkci.

- Kvantifikátory jsou ve výchozím stavu **hladové**: odpovídají co nejvíce. Koncové
  `?` udělá jeden **líným** (`\d+?` odpovídá co nejmenšímu počtu číslic).
- Kvantifikátor se vztahuje na jedinou položku před ním — znak, třídu nebo skupinu v
  závorkách: `(ab)+` odpovídá `ababab`.

```python
import re

re.findall(r"[A-Za-z]+", "Hello, world!")   # ['Hello', 'world']
re.findall(r"\d{4}", "y2024 y2025")          # ['2024', '2025']
re.search(r"colou?r", "color")               # matches (the u is optional)
```
