Řetězec je uspořádaná posloupnost znaků a `s[index]` přečte ten na dané pozici.
Pozice jsou **číslovány od nuly**: první znak je `s[0]`, druhý `s[1]` a tak dále.

- Výsledek je sám o sobě jednoznakový řetězec (Python nemá samostatný typ pro
  znak).
- Index rovný délce nebo větší vyvolá `IndexError`; pro řetězec délky *n* jsou
  platné pozice `0` až `n - 1`.
- Řetězce jsou **neměnné** — indexování znak přečte, ale `s[0] = "x"` je chyba.
  Pro změnu textu vytvoříš nový řetězec.

```python
word = "Python"
word[0]    # 'P'
word[3]    # 'h'
```
