Otevření v režimu **`"w"`** otevře soubor pro **zápis**. Soubor **vytvoří**, pokud
chybí, a **zkrátí** ho (vyprázdní), pokud už existuje, takže stávající obsah se
ztratí.

- **`f.write(text)`** zapíše řetězec a, na rozdíl od `print`, **nepřidá** žádné
  koncové zalomení — zahrň `"\n"` sám tam, kde chceš zalomení řádků.
- `f.write` bere jen řetězce; čísla nejprve převeď pomocí `str()` nebo f-řetězce.
- Použij `with`, aby se data vyprázdnila do souboru a soubor se správně zavřel.

```python
with open("out.txt", "w") as f:
    f.write("first line\n")
    f.write("second line\n")   # newlines are explicit
```
