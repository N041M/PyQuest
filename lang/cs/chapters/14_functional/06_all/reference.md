**`all(iterable)`** vrátí `True` jen tehdy, když je **každá** položka pravdivá —
partner k `any`. Odpoví na „projdou všechny?“ jedním výrazem.

- Vyhodnocuje se **zkráceně** u první nepravdivé položky a okamžitě vrátí `False`.
- `all([])` je `True` — *prázdně* (vacuously), protože žádná položka neselhala. Toto
  pravidlo „všechny z ničeho je pravda“ je častý překvap; ošetři prázdný případ,
  pokud na něm záleží.
- Stejný tvar jako `any`: `all(<test> for <item> in <iterable>)`. Dohromady
  vyjadřují univerzální („pro všechny“) a existenční („existuje“) otázku nad
  posloupností.

```python
all(n > 0 for n in [1, 2, 3])     # True
all(n > 0 for n in [1, -2, 3])    # False
all([])                           # True  -- vacuously
```
