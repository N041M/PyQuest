Závěrečná úloha je úplný **okruh tam a zpět** skrz modul, skládající tři jeho
nástroje:

1. **Parsuj** — `datetime.strptime(timestamp, "%Y-%m-%d %H:%M")` přečte řetězec na
   `datetime`.
2. **Posuň** — přičtení `timedelta(hours=h)` ho posune o dobu, přecházejíc napříč
   minutami, dny, měsíci a roky automaticky (a dozadu pro záporné `h`).
3. **Naformátuj** — `.strftime("%Y-%m-%d %H:%M")` vykreslí výsledek zpět do stejného
   rozvržení.

Smysl kapitoly v jedné funkci: každá nepříjemná hrana — čas přecházející půlnoc, den
přecházející do nového měsíce nebo roku, přestupný den — je zpracována typy
`datetime`, ne tebou. Ty popíšeš kroky; knihovna drží kalendář poctivý.

```python
from datetime import datetime, timedelta

def add_hours(timestamp, hours):
    dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M")
    return (dt + timedelta(hours=hours)).strftime("%Y-%m-%d %H:%M")

add_hours("2026-06-20 23:30", 2)    # '2026-06-21 01:30'
```
