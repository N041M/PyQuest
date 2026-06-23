**Boolean** je jedna ze dvou hodnot, `True` nebo `False` (typ `bool`).
**Porovnávací operátory** ho vytvoří porovnáním dvou hodnot:

- `==` rovno, `!=` nerovno,
- `<` menší než, `>` větší než, `<=` nejvýše, `>=` nejméně.

`==` (otázka „rovnají se?“) není `=` (příkaz „přiřaď“). Čísla se porovnávají podle
hodnoty; řetězce se porovnávají **lexikograficky** (slovníkové pořadí, podle kódu
znaku, takže velká písmena se řadí před malá). Porovnání lze **řetězit**:
`0 <= x < 10` znamená `0 <= x and x < 10`.

```python
3 < 5        # True
3 == 3.0     # True   -- equal values, different types
"a" < "b"    # True
```
