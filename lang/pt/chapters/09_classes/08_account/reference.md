O capstone é uma **classe com estado** que junta o capítulo todo: um valor
por omissão em `__init__`, métodos que **alteram** o estado, uma **guarda**
que lança um erro em operações inválidas, e `__str__` para exibição.

- `__init__` define o saldo inicial (com um valor por omissão); `deposit` e
  `withdraw` alteram `self.balance` no próprio lugar.
- Uma guarda protege o invariante: `withdraw` verifica os fundos e
  `raise ValueError(...)` em vez de permitir um estado impossível.
- `__str__` representa o objeto para impressão. Juntas, estas peças fazem um
  objeto fiável de usar e agradável de ler.

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
