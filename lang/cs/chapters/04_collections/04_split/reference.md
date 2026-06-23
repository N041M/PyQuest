**`s.split()`** rozdělí řetězec na **seznam kousků**. Bez argumentu dělí podle
úseků **bílých znaků** a zahodí mezery na začátku a konci — obvyklý způsob, jak
získat slova řádku.

- `s.split(sep)` dělí podle přesného oddělovače `sep` a ponechává prázdné kousky
  mezi sousedními oddělovači (`"a,,b".split(",")` je `["a", "", "b"]`).
- `s.split(sep, maxsplit)` dělí nejvýše `maxsplit`krát — hodí se k odloupnutí
  předpony, např. `"key=a=b".split("=", 1)` je `["key", "a=b"]`.
- Je to inverze k `join` (další).

```python
"the quick fox".split()        # ['the', 'quick', 'fox']
"2024-01-15".split("-")        # ['2024', '01', '15']
```
