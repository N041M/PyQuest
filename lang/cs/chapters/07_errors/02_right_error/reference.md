`except` by měl pojmenovat **konkrétní** výjimku, kterou čekáš. Zachycení přesně
správného typu nechá nečekané chyby vyplout jako bugy, místo aby byly tiše
spolknuty.

- `except ValueError:` chytá jen tento typ; nesouvisející selhání (překlep ve
  jméně vyvolávající `NameError`) se stále šíří dál, což je to, co chceš.
- Holé `except:` (nebo `except Exception:`) chytá **všechno**, včetně bugů, které
  bys raději viděl — vyhni se mu, pokud opravdu nemyslíš „jakékoli selhání“.
- Přizpůsob typ operaci: `int()` vyvolá `ValueError`, indexování `IndexError`,
  vyhledání ve slovníku `KeyError`.

```python
try:
    value = data[key]
except KeyError:         # only a missing key, not other bugs
    value = None
```
