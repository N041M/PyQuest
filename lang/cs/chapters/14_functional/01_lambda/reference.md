**`lambda`** je anonymní funkce psaná jako jediný výraz: `lambda args: expression`.
Hodnota výrazu se vrátí automaticky — není tu žádné `return` a tělo musí být
**jeden** výraz.

- lambda je prvotřídní **hodnota**: přiřaď ji, vrať ji nebo ji předej jako argument.
  `f = lambda x: x * 2` je hodně podobné `def f(x): return x * 2`, jen inline a bez
  jména.
- Definovaná uvnitř jiné funkce lambda **uzavře** proměnné toho rozsahu —
  `lambda x: x * n` zachytí `n` odtud, kde byla vytvořena, takže každé
  `multiplier(n)` dá funkci svázanou s vlastním `n`.
- Lambdy jsou pro *malé* inline funkce, hlavně jako `key=` pro `sorted` nebo funkce
  pro `map`/`filter` (zbytek této kapitoly). Na cokoli s více příkazy použij
  pojmenovaný `def`.

```python
double = lambda x: x * 2
double(5)                  # 10

def multiplier(n):
    return lambda x: x * n
multiplier(3)(4)           # 12
```
