Argument **`key=`** od `sorted` je funkce mapující každou položku na hodnotu, podle
níž se řadí, takže můžeš řadit podle něčeho **odvozeného** z položek, ne podle
samotných položek. Inline **`lambda`** je idiomatický způsob, jak ten klíč napsat.

- `key` se volá **jednou na položku**; `sorted` položky seřadí podle výsledných
  hodnot klíče, ale vrátí původní položky. `sorted(words, key=len)` řadí podle délky,
  `sorted(words, key=lambda w: w[-1])` podle posledního písmene.
- `sorted` je **stabilní**: položky se stejnými klíči si ponechají vstupní pořadí.
- Spoj `key=` s **`reverse=True`** k sestupnému řazení. Stejné `key=` funguje na
  `list.sort`, `min` a `max`.

```python
sorted(["pear", "fig", "apple"], key=len)            # ['fig', 'pear', 'apple']
sorted([-3, 1, -2], key=lambda n: abs(n))            # [1, -2, -3]
sorted(records, key=lambda r: r[1], reverse=True)    # by 2nd field, high first
```
