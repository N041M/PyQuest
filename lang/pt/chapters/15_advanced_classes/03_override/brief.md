# 15.3 -- Sobreposição: a versão própria de um filho

## Conceito

Uma subclasse pode **sobrepor** um método do pai -- definir a sua própria
versão de um método que o pai já tem. Para as instâncias da subclasse, a nova
versão prevalece:

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "..."          # generic

class Cat(Animal):
    def speak(self):
        return "Meow"         # Cat's own
```

- `Cat("Felix").speak()` devolve `"Meow"`; um simples `Animal(...).speak()`
  continua a devolver `"..."`.
- Isto é **polimorfismo**: a *mesma* chamada, `x.speak()`, faz a coisa certa
  para qualquer que seja o tipo de `x`.
- A subclasse continua a herdar tudo o que não sobrepõe (aqui, `__init__` e
  `self.name`).

## A tua tarefa

Define `Animal` com `__init__(self, name)` e `speak(self)` a devolver `"..."`.
Depois define `Cat(Animal)` que **sobrepõe** `speak` para devolver `"Meow"`.

## Está feito quando

- `Cat("Felix").speak()` devolve `"Meow"`.
- `Animal("thing").speak()` devolve `"..."` (inalterado).
- `Cat("Felix").name` é `"Felix"` (`__init__` herdado), e um Cat é um Animal.
