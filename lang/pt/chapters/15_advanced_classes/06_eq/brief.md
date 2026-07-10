# 15.6 -- __eq__: igualdade de valor

## Conceito

Por omissão, `==` em objetos pergunta "são o **mesmo objeto**?" -- por isso
dois objetos construídos separadamente com dados idênticos *não* são iguais.
O método dunder **`__eq__`** muda isso para **igualdade de valor**:

```python
class Money:
    def __init__(self, cents):
        self.cents = cents
    def __eq__(self, other):
        return self.cents == other.cents

Money(500) == Money(500)     # True   -- same value
Money(500) == Money(750)     # False
```

- O Python chama `a.__eq__(b)` para `a == b`. Devolves se devem ser
  considerados iguais -- normalmente comparando os atributos que definem o
  valor.
- `!=` é tratado por ti (é a negação de `__eq__`).
- (Definir `__eq__` também é o que permite que os teus objetos sejam
  comparados por valor em testes, listas, e verificações com `in`.)

## A tua tarefa

Define `Money` com `__init__(self, cents)` e um **`__eq__`** para que dois
objetos `Money` sejam iguais exatamente quando os seus `cents` coincidem.

## Está feito quando

- `Money(500) == Money(500)` é `True`.
- `Money(500) == Money(750)` é `False`.
- A igualdade compara `cents`, não a identidade do objeto.
