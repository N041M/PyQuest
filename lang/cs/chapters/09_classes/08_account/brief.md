# 9.8 -- Závěrečná: bankovní účet

## Koncept

Čas spojit kapitolu: třída se stavem, několik metod, rozumná výchozí hodnota a
pravidlo, které vymáhá.

`BankAccount` drží `balance`. Můžeš vložit (roste) i vybrat (klesá) -- ale výběr,
který by účet přečerpal, musí být **odmítnut** a zůstatek ponechán beze změny.

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

- `balance` má výchozí hodnotu `0`, takže `BankAccount()` je prázdný účet.
- `deposit` a `withdraw` mění uložený zůstatek (stav, který přetrvává).
- `withdraw` **vrátí `True`**, když uspěje, a **`False`**, když odmítne -- a při
  odmítnutí se zůstatek nemění.

```python
acc = BankAccount(100)
acc.deposit(50)       # balance 150
acc.withdraw(70)      # True,  balance 80
acc.withdraw(999)     # False, balance still 80
```

## Tvůj úkol

Definuj `BankAccount` přesně jako výše: `balance` s výchozí hodnotou `0`, metodu
`deposit(amount)` a metodu `withdraw(amount)`, která odečte a vrátí `True` jen
tehdy, když je dost prostředků -- jinak nic nezmění a vrátí `False`.

## Hotovo, když

- `BankAccount()` začne na `0`; `BankAccount(100)` začne na `100`.
- `deposit` a `withdraw` aktualizují `balance` a výběr příliš velký vrátí `False` a
  nechá `balance` beze změny.
- Výběr přesně zůstatku je povolen.
