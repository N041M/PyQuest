Řetězec je **iterovatelný**, takže cyklus `for` ho prochází **po jednom znaku**,
v pořadí, přičemž řídicí proměnnou naváže na každý znak. Neindexuješ ručně.

- Každý průchod dá jednoznakový řetězec; cyklus proběhne `len(s)`krát.
- Tohle je přímý způsob, jak zkoumat nebo počítat znaky — spoj to s `if` uvnitř
  cyklu, abys reagoval na určité z nich.
- Stejný tvar `for ... in` prochází libovolnou posloupnost (seznamy, rozsahy, …),
  ne jen řetězce.

```python
for ch in "cat":
    print(ch)             # c, then a, then t
```
