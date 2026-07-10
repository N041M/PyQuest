Por omissão, `==` entre objetos testa a **identidade** — se são exatamente o
mesmo objeto — por isso dois objetos construídos de forma independente com
dados idênticos comparam como diferentes. Definir **`__eq__(self, other)`**
redefine `==` como **igualdade de valor**.

- O Python chama `a.__eq__(b)` para avaliar `a == b`; devolve se devem contar
  como iguais, normalmente comparando os atributos que definem o valor. `!=`
  segue-se automaticamente como a sua negação.
- A igualdade de valor é o que faz os objetos funcionarem de forma intuitiva
  em testes com `==`, na pertença a `list` (`in`), e ao comparar resultados.
- Se definires `__eq__`, a classe torna-se **não hasheável** (o seu
  `__hash__` é definido como `None`), pelo que não pode entrar num `set` ou
  ser chave de `dict` até também definires `__hash__` — muitas vezes
  `return hash(self.cents)`.

```python
class Money:
    def __init__(self, cents): self.cents = cents
    def __eq__(self, other): return self.cents == other.cents

Money(500) == Money(500)     # True
Money(500) == Money(750)     # False
```
