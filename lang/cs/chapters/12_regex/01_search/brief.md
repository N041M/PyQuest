# 12.1 -- re.search: je tam ten vzor?

## Koncept

**Regulární výraz** („regex“) je malý jazyk pro popis vzorů v textu. Modul **`re`**
je hledá. Nejzákladnější otázka je „objevuje se tento vzor někde?“ -- **`re.search`**:

```python
import re

re.search(r"\d", "abc4")     # a match object (truthy)
re.search(r"\d", "abc")      # None
```

- Vzor se píše jako **surový řetězec** `r"..."`, aby zpětná lomítka znamenala to, co
  regex očekává (`r"\d"`, ne `"\d"`).
- `\d` odpovídá libovolné jediné **číslici**. Další zkratky: `\w` znak slova, `\s`
  bílý znak, `.` libovolný znak.
- `re.search` vrátí **objekt shody** (match object), pokud se vzor najde kdekoli,
  nebo **`None`**, pokud ne -- takže `re.search(...) is not None` je čisté ano/ne.

## Příklad

```python
import re

def has_letter(text):
    return re.search(r"[a-z]", text) is not None
```

## Tvůj úkol

Pomocí **`re.search`** definuj `has_digit(text)`, která vrátí `True`, pokud `text`
obsahuje alespoň jednu číslici, jinak `False`.

## Hotovo, když

- `has_digit("abc4")` je `True`, `has_digit("abc")` je `False`.
- `has_digit("")` je `False`.
- Test používá `re.search` s `\d`, ne ručně psané hledání číslic.
