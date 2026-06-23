**`except ValueError as e:`** naváže zachycený **objekt** výjimky na jméno, takže
ho můžeš prozkoumat — nejjednodušeji jeho vypsáním, abys ukázal, co se pokazilo.

- Objekt výjimky nese detail; `str(e)` (nebo `print(e)`) dá jeho zprávu.
  `type(e).__name__` dá jméno třídy chyby.
- Jméno `e` existuje jen uvnitř bloku `except`.
- Jeden handler může chytit celou rodinu pojmenováním základní třídy:
  `except Exception as e:` naváže kteroukoli z jejích podtříd (používej střídmě —
  široké chytání skrývá bugy).

```python
try:
    int("xyz")
except ValueError as e:
    print("bad input:", e)    # bad input: invalid literal for int()...
```
