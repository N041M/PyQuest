Python má tři operátory dělení:

- **`/` pravé dělení** vždy vytvoří **`float`**, i když je výsledek celé číslo:
  `7 / 2 == 3.5` a `4 / 2 == 2.0` (všimni si `.0`).
- **`//` celočíselné dělení** dělí a zaokrouhluje *dolů* k zápornému nekonečnu, u
  dvou celých čísel dává `int`: `7 // 2 == 3`. Se záporným operandem stále
  zaokrouhluje dolů, takže `-7 // 2 == -4`, ne `-3`.
- **`%` zbytek (modulo)** je to, co zbude: `7 % 2 == 1`. V Pythonu má výsledek
  **znaménko dělitele**, takže `-7 % 2 == 1`.

Pro libovolná celá čísla platí `a == (a // b) * b + (a % b)`. `divmod(a, b)` vrátí
dvojici `(a // b, a % b)` najednou. Dělení nulou vyvolá `ZeroDivisionError`.

```python
17 / 5    # 3.4
17 // 5   # 3
17 % 5    # 2   -- 3*5 + 2 == 17
```
