Závěrečná úloha je **stavová třída**, která spojuje kapitolu: výchozí hodnota v
`__init__`, metody, které **mutují** stav, **stráž**, která vyvolá chybu při
neplatných operacích, a `__str__` pro zobrazení.

- `__init__` nastaví počáteční zůstatek (s výchozí hodnotou); `deposit` a
  `withdraw` mění `self.balance` na místě.
- Stráž chrání invariant: `withdraw` zkontroluje prostředky a
  `raise ValueError(...)`, místo aby povolil nemožný stav.
- `__str__` vykreslí objekt pro tisk. Dohromady to dělá objekt, který je spolehlivé
  používat a příjemné číst.

```python
class Account:
    def __init__(self, balance=0):
        self.balance = balance
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount
    def __str__(self):
        return f"balance: {self.balance}"
```
