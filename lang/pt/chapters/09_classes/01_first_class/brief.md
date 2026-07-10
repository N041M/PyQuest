# 9.1 -- A primeira classe

## Conceito

Uma **classe** é um molde para um objeto que junta dados relacionados. Até
agora, o nome e a idade de um cão seriam duas variáveis soltas; uma classe
une-as numa única coisa que podes passar de um lado para o outro.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

- `class Dog:` dá nome ao molde.
- `__init__` é o **construtor** -- corre quando constróis um novo Dog, e a sua
  função é preparar os dados do objeto.
- `self` é o objeto que está a ser construído; `self.name = name` guarda o
  valor **no objeto** para que continue lá mais tarde.

Constróis um (uma *instância*) chamando a classe como se fosse uma função, e
lês os seus dados com um ponto:

```python
d = Dog("Rex", 3)
print(d.name)   # Rex
print(d.age)    # 3
```

## A tua tarefa

Define uma classe `Dog` cujo `__init__` recebe um `name` e uma `age` e guarda
cada um no objeto como `self.name` e `self.age`.

## Está feito quando

- `Dog("Rex", 3)` cria um objeto cujo `.name` é `"Rex"` e `.age` é `3`.
- Funciona para qualquer nome e idade.
- Usaste uma `class` com um `__init__` que guarda os dois valores em `self`.
