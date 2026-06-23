Seznam je iterovatelný, takže **`for x in lst`** navštíví každou položku v pořadí
a naváže řídicí proměnnou na samotnou položku (ne na její index).

- Tohle je obvyklý způsob, jak číst seznam. Když potřebuješ i pozici, spoj to s
  `range(len(lst))` nebo `enumerate` (kapitola 5).
- **`len(lst)`** dá počet položek; **řez** (`lst[1:3]`, `lst[::-1]`) funguje přesně
  jako u řetězců a vrací nový seznam.

```python
for name in ["Ada", "Linus"]:
    print(name)

total = 0
for n in [3, 1, 4]:
    total += n           # iterate and accumulate
```
