**Slovník** (`dict`) mapuje **klíče** na **hodnoty**: `{"a": 1, "b": 2}`. Je to
nástroj pro vyhledávání podle jména, ne podle pozice.

- **`d[key]`** přečte hodnotu pro klíč; **`d[key] = value`** klíč přidá (je-li
  nový) nebo aktualizuje (je-li přítomen). Klíče jsou jedinečné — přiřazení
  existujícího klíče přepíše.
- Čtení **chybějícího** klíče pomocí `d[key]` vyvolá `KeyError` (viz `.get`, 4.10).
- Klíče musí být neměnné (řetězce, čísla, n-tice); hodnoty mohou být cokoli.
  `len(d)` počítá páry; `key in d` testuje přítomnost klíče.

```python
ages = {"Ada": 36}
ages["Ada"]          # 36
ages["Linus"] = 21   # add a new pair
```
