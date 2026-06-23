**Vrácení** hodnoty a její **vypsání** jsou různé činy a jejich záměna je častá
chyba.

- **`return`** předá hodnotu zpět volajícímu kódu, který ji může uložit, počítat s
  ní nebo ji poslat dál. Hodnota putuje.
- **`print`** zapíše text na obrazovku a vrátí `None`. Hodnota se zobrazí, ale
  nezachytí — `x = print(5)` udělá z `x` `None`.
- Na funkci, která místo vracení vypisuje, nelze stavět. Dej přednost `return`
  výsledku a nech **volajícího** rozhodnout, zda ho vypsat.

```python
def double(n):
    return n * 2        # caller can use it
print(double(5) + 1)    # 11  -- works because double returned
```
