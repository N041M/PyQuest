`__init__` é uma função comum, por isso os seus parâmetros podem ter
**valores por omissão** — permitindo criar um objeto com ou sem determinados
argumentos.

- `def __init__(self, balance=0):` permite `Account()` (começa em 0) ou
  `Account(100)` (começa em 100).
- Aplicam-se as mesmas regras: os parâmetros com valor por omissão vêm depois
  dos que não têm, e um valor por omissão mutável precisa do truque do
  sentinela `None`
  (`def __init__(self, items=None): self.items = items or []`).
- Os valores por omissão tornam o caso comum simples, mantendo a opção em
  aberto.

```python
class Account:
    def __init__(self, balance=0):
        self.balance = balance

Account().balance        # 0
Account(100).balance     # 100
```
