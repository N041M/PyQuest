Indexování za konec seznamu (nebo řetězce) vyvolá **`IndexError`**. Jeho zachycení
promění rizikové vyhledání v **bezpečný přístup**, který vrátí náhradní hodnotu,
když pozice neexistuje.

- `lst[i]` vyvolá chybu, je-li `i >= len(lst)` (nebo `i < -len(lst)`); `except`
  místo pádu dodá výchozí hodnotu.
- Tohle je EAFP protějšek kontroly `if i < len(lst):` napřed — užitečné, když je
  případ mimo rozsah normální, ne bug.

```python
def get(lst, i, default=None):
    try:
        return lst[i]
    except IndexError:
        return default   # position absent -> fallback
```
