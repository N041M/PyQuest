Řetězce nesou **metody** — funkce volané syntaxí `s.metoda()`, které z řetězce
něco spočítají.

- **`.strip()`** vrátí řetězec s odstraněnými **bílými znaky** na začátku a konci
  (mezery, tabulátory, nové řádky). `.lstrip()` / `.rstrip()` oříznou jednu
  stranu.
- **`.upper()`** / **`.lower()`** vrátí řetězec s každým písmenem velkým, resp.
  malým.

Protože každá metoda vrací **nový** řetězec (originál se nikdy nezmění), volání se
**řetězí**: každé působí na výsledek předchozího.

```python
"  Hi  ".strip()            # 'Hi'
"Hi".upper()                # 'HI'
"  Hello  ".strip().lower() # 'hello'  -- trimmed, then lowered
```
