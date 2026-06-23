# 12.2 -- re.findall: každá shoda

## Koncept

`re.search` najde *první* shodu. **`re.findall`** vrátí **všechny**, jako seznam
řetězců:

```python
import re

re.findall(r"\d+", "a12b3c456")     # ['12', '3', '456']
```

- `\d+` znamená „jedna nebo více číslic“ -- `+` přiměje vzor pochytat celý úsek
  číslic, ne jen jednu. Takže každá shoda je celé číslo.
- `re.findall` vrátí **seznam řetězců** (nalezený text), zleva doprava,
  nepřekrývající se. Žádná shoda dá prázdný seznam `[]`.
- Shody jsou stále text; převeď pomocí `int(...)`, pokud chceš čísla.

## Příklad

```python
import re

def words(text):
    return re.findall(r"[a-z]+", text)
```

## Tvůj úkol

Pomocí **`re.findall`** definuj `all_numbers(text)`, která vrátí seznam každého úseku
číslic v `text`, jako řetězce.

## Hotovo, když

- `all_numbers("a12b3c456")` vrátí `["12", "3", "456"]`.
- `all_numbers("nothing")` vrátí `[]`.
- Extrakce používá `re.findall` s `\d+`, ne ručně psané hledání.
