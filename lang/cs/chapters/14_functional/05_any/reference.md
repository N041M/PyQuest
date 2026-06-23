**`any(iterable)`** vrátí `True`, jakmile je **jedna** položka pravdivá, jinak
`False`. Když dostane generátor testů, odpoví na „projde nějaká položka?“ jediným
výrazem a nahradí cyklus, který nastavuje příznak.

- Vyhodnocuje se **zkráceně**: vyhodnocování se zastaví u první pravdivé položky,
  takže je efektivní a funguje na nekonečných/líných iterovatelných objektech.
- `any([])` je `False` — není tu nic, co by bylo pravda.
- Idiom je `any(<test> for <item> in <iterable>)`: generátorový výraz booleanů.
  (Jeho partner `all` je 14.6.)

```python
any(n < 0 for n in [1, 2, -3])    # True
any(c.isdigit() for c in "abc")   # False
any([])                           # False
```
