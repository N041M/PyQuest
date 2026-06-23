**Parametr** je jméno v hlavičce funkce, které zastupuje hodnotu dodanou
volajícím. Hodnoty předané ve volání jsou **argumenty**, přiřazené parametrům
zleva doprava.

- `def f(a, b):` deklaruje dva parametry; `f(3, 4)` volá s `a = 3`, `b = 4`.
- Parametry jsou **lokální**: existují jen po dobu volání a nesrážejí se se jmény
  venku. Funkce pracuje s tím, co dostane, což ji činí znovupoužitelnou.
- Předání špatného počtu argumentů vyvolá `TypeError`.

```python
def add(a, b):
    return a + b

add(3, 4)      # 7
```
