# 9.8 -- Capstone: uma conta bancária

## Conceito

Chegou a hora de juntar o capítulo todo: uma classe com estado, vários
métodos, um valor por omissão sensato, e uma regra que ela própria impõe.

Uma `BankAccount` mantém um `balance`. Podes depositar (cresce) e levantar
(diminui) -- mas um levantamento que deixasse a conta a descoberto tem de ser
**recusado**, mantendo o saldo intocado.

```python
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False
```

- `balance` tem por omissão `0`, por isso `BankAccount()` é uma conta vazia.
- `deposit` e `withdraw` alteram o saldo guardado (estado que persiste).
- `withdraw` **devolve `True`** quando tem sucesso e **`False`** quando
  recusa -- e, ao recusar, o saldo não muda.

```python
acc = BankAccount(100)
acc.deposit(50)       # balance 150
acc.withdraw(70)      # True,  balance 80
acc.withdraw(999)     # False, balance still 80
```

## A tua tarefa

Define `BankAccount` exatamente como acima: um `balance` com valor por
omissão `0`, um método `deposit(amount)`, e um método `withdraw(amount)` que
subtrai e devolve `True` só quando há saldo suficiente -- caso contrário não
muda nada e devolve `False`.

## Está feito quando

- `BankAccount()` começa em `0`; `BankAccount(100)` começa em `100`.
- `deposit` e `withdraw` atualizam `balance`, e levantar demasiado devolve
  `False` e deixa `balance` inalterado.
- Levantar exatamente o saldo é permitido.
