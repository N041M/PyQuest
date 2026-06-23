Řez má třetí část, **krok**: `s[start:stop:step]` vezme každý `step`-tý znak.
Výchozí krok je 1.

- `s[::2]` vezme každý druhý znak (indexy 0, 2, 4, …).
- **Záporný** krok jde pozpátku. `s[::-1]` je idiomatický způsob, jak **obrátit**
  řetězec; se záporným krokem se výchozí start/stop přehodí na konec a začátek.
- `s[::-2]` vezme každý druhý znak, od konce směrem k začátku.

```python
s = "Python"
s[::2]    # 'Pto'
s[::-1]   # 'nohtyP'  -- reversed
```
