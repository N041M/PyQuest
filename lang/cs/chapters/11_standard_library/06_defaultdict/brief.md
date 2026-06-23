# 11.6 -- defaultdict: výchozí hodnota pro chybějící klíče

## Koncept

Abys seskupil položky v prostém slovníku, musíš nejdřív zkontrolovat, zda klíč
existuje:

```python
if length not in groups:
    groups[length] = []
groups[length].append(word)
```

**`defaultdict`** tento obřad odstraní. Dáš mu **továrnu** (factory) -- funkci, která
vytvoří výchozí hodnotu -- a on tu továrnu zavolá automaticky, když se poprvé dotkneš
chybějícího klíče:

```python
from collections import defaultdict

groups = defaultdict(list)     # missing key -> a fresh []
groups[5].append("hello")      # no setup needed
```

- `defaultdict(list)` vytvoří prázdný seznam pro každý nový klíč, takže `.append`
  prostě funguje.
- `defaultdict(int)` vytvoří `0` pro každý nový klíč -- sčítání bez `.get`.
- Jinak je to skutečný slovník; převeď pomocí `dict(groups)`, pokud chceš prostý.

## Příklad

```python
from collections import defaultdict

def by_first_letter(words):
    groups = defaultdict(list)
    for w in words:
        groups[w[0]].append(w)
    return dict(groups)
```

## Tvůj úkol

Pomocí **`defaultdict`** z `collections` definuj `group_by_length(words)`, která
vrátí slovník mapující každou **délku** slova na seznam slov té délky, v jejich
původním pořadí.

## Hotovo, když

- `group_by_length(["hi", "ok", "bye"])` se rovná `{2: ["hi", "ok"], 3: ["bye"]}`.
- `group_by_length([])` se rovná `{}`.
- Seskupování používá `defaultdict(list)`, ne ruční kontrolu „if key in dict“.
