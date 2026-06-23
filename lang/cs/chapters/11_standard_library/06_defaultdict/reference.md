**`defaultdict`** (z **`collections`**) je `dict`, který automaticky dodá výchozí
hodnotu pro chybějící klíč. Předáš mu **továrnu** — bezargumentový volatelný objekt,
který sestaví výchozí hodnotu — a když poprvé přečteš nebo se dotkneš nepřítomného
klíče, zavolá továrnu, výsledek uloží a použije.

- `defaultdict(list)` vytvoří čerstvý `[]` pro každý nový klíč, takže
  `d[k].append(x)` funguje bez nastavení „if key not in d“ — idiom seskupování.
- `defaultdict(int)` vytvoří `0` pro každý nový klíč, takže `d[k] += 1` sčítá.
- Továrnu spustí jen **vyhledání** chybějícího klíče; jinak je to obyčejný slovník.
  `dict(d)` převede na prostý slovník a *skutečně* chybějící klíč se stále čte jako
  výchozí, místo aby vyvolal chybu.

```python
from collections import defaultdict

groups = defaultdict(list)
groups[5].append("hello")    # key 5 auto-starts as []
groups                       # defaultdict(<class 'list'>, {5: ['hello']})
```
