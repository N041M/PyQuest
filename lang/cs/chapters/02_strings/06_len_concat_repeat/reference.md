Tři základní operace s řetězci:

- **`len(s)`** vrátí počet znaků v `s` jako `int`; `len("")` je `0`.
- **`+` zřetězí**: `"ab" + "cd"` je `"abcd"`. Oba operandy musí být řetězce —
  `"n" + 5` vyvolá `TypeError`; nejprve převeď pomocí `str(5)`.
- **`*` opakuje**: `s * n` (nebo `n * s`) spojí `n` kopií. `"ab" * 3` je
  `"ababab"`; `n <= 0` dá prázdný řetězec `""`.

Všechny tři vytvoří **nové** řetězce a originály nechají beze změny (řetězce jsou
neměnné).

```python
s = "ab"
len(s)    # 2
s + "c"   # 'abc'
s * 3     # 'ababab'
```
