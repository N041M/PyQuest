Umístění **`yield` dovnitř cyklu** proudí celou posloupnost: generátor vydá jednu
transformovanou hodnotu na průchod, pozastaví se po každé a obnoví se na další
požadavek.

- `for x in source: yield f(x)` vyzve `f(x)` pro každou položku — generátorová
  podoba stavění seznamu komprehenzí, ale produkovaná líně.
- Nic se nespočítá, dokud něco generátor neprochází, a jen do té míry, do jaké se
  konzumuje.

```python
def squares(nums):
    for n in nums:
        yield n * n

list(squares([1, 2, 3]))    # [1, 4, 9]
```
