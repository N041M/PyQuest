**`Counter`** (z modulu **`collections`**) je podtřída `dict`, která sečte
iterovatelný objekt jedním voláním: `Counter(items)` vrátí mapování každé odlišné
položky na to, kolikrát se objeví — cyklus `counts.get(k, 0) + 1`, už napsaný.

- Jelikož je to slovník, podporuje vše, co slovník (`c[key]`, `c.items()`,
  `key in c`), a porovnává se jako **rovný** prostému slovníku se stejnými počty.
- **Chybějící** klíč se čte jako `0`, místo aby vyvolal `KeyError`, což sčítání
  vyhovuje.
- **`c.most_common(n)`** vrátí `n` dvojic `(položka, počet)` s nejvyšším počtem, už
  seřazených — krok zprávy zadarmo. Countery se také sčítají a odčítají (`c1 + c2`),
  aby zkombinovaly součty.

```python
from collections import Counter

c = Counter("banana")     # Counter({'a': 3, 'n': 2, 'b': 1})
c["a"]                    # 3
c["z"]                    # 0  -- no KeyError
c.most_common(1)          # [('a', 3)]
```
