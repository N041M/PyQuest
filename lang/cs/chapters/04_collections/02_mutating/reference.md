Seznamy jsou **měnitelné**: jejich obsah se může měnit na místě, na rozdíl od
řetězců.

- **`lst[i] = x`** nahradí položku na indexu `i`. Index už musí existovat
  (přiřazení za konec vyvolá `IndexError`).
- **`.pop()`** odebere a **vrátí** poslední položku a zmenší seznam; `.pop(i)`
  odebere položku na indexu `i`. Pop z prázdného seznamu vyvolá chybu.
- Další změny na místě: `.insert(i, x)`, `.remove(value)`, `del lst[i]`.

Protože změna je na místě, vidí ji každé jméno odkazující na tentýž objekt seznamu.

```python
lst = [10, 20, 30]
lst[1] = 99      # [10, 99, 30]
last = lst.pop() # last == 30, lst == [10, 99]
```
