# 11.5 -- Counter: sčítání v jednom kroku

## Koncept

Zpět v kapitole 5 jsi sčítal ručně: `counts[k] = counts.get(k, 0) + 1`. Modul
**`collections`** dodává tento vzor, napsaný a otestovaný, jako **`Counter`**:

```python
from collections import Counter

Counter("banana")     # Counter({'a': 3, 'n': 2, 'b': 1})
```

- `Counter(items)` projde libovolný iterovatelný objekt a vrátí počet každé odlišné
  položky.
- `Counter` **je** slovník (je to podtřída), takže `counts[x]` i
  `for k, v in counts.items()` fungují přesně, jak bys čekal -- a porovnává se jako
  rovný prostému slovníku se stejnými počty.
- Zvládá dokonce chybějící klíč: `counts["zzz"]` je `0`, ne `KeyError`.

To je slib standardní knihovny: cyklus, který bys napsal, už je nástroj.

## Příklad

```python
from collections import Counter

def letter_counts(word):
    return Counter(word)
```

## Tvůj úkol

Pomocí **`Counter`** z `collections` definuj `tally(items)`, která vrátí počet, kolikrát se každá položka objeví v seznamu `items`.

## Hotovo, když

- `tally(["a", "b", "a"])` se rovná `{"a": 2, "b": 1}`.
- `tally([])` se rovná `{}`.
- Počítání dělá `Counter`, ne ručně psaný cyklus.
