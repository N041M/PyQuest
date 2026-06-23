Funkce **volají jiné funkce**, takže větší úloha se staví z malých, ověřených
dílů. Výsledek jedné se stává argumentem nebo stavebním kamenem další.

- Pomocná funkce dělá jednu věc dobře; funkce vyšší úrovně volá několik pomocných
  a kombinuje jejich výsledky. To je jádro strukturování programu.
- `f(g(x))` předá výsledek `g` rovnou do `f`. Každá funkce zůstává jednoduchá a
  nezávisle ověřitelná.

```python
def clean(s):  return s.strip().lower()
def is_yes(s): return clean(s) == "yes"

is_yes("  YES ")   # True  -- is_yes builds on clean
```
