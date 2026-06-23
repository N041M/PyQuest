Operátor **`in`** testuje příslušnost a dává boolean, takže ho zasadíš rovnou do
`if` nebo `while`. `x in c` je `True`, když je `x` nalezeno v `c`.

- U **řetězce** `in` testuje **podřetězec**: `"cat" in "concatenate"` je `True`.
- U **seznamu** nebo **n-tice** testuje položku (prochází posloupnost).
- U **slovníku** nebo **množiny** testuje **klíč**/člena — a je rychlé (založené na
  hashování), na rozdíl od lineárního procházení seznamu.
- `x not in c` je čitelná negace.

```python
"a" in "cat"          # True
3 in [1, 2, 3]        # True
"key" in {"key": 1}   # True  -- tests keys
```
