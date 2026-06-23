**Sčítací** vzor počítá, kolikrát se každá odlišná věc objeví, pomocí slovníku,
jehož klíče jsou ty věci a jehož hodnoty jsou průběžné počty.

- Pro každou položku `counts[k] = counts.get(k, 0) + 1` přečte aktuální počet (`0`,
  když je klíč viděn poprvé, díky výchozí hodnotě `.get`) a zapíše o jeden víc.
- Začni z prázdného slovníku `{}`; klíče se objevují, jak jsou poprvé potkány.
- `collections.Counter` ze standardní knihovny to udělá v jednom kroku, ale idiom
  `.get(k, 0) + 1` ukazuje přesně, co se děje.

```python
counts = {}
for w in ["a", "b", "a"]:
    counts[w] = counts.get(w, 0) + 1   # {'a': 2, 'b': 1}
```
