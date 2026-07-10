# 15.1 -- Herança: construir a partir de uma classe base

## Conceito

O Capítulo 9 construiu classes isoladas. A **herança** permite que uma classe se
construa a partir de outra: uma **subclasse** obtém automaticamente os métodos da
**classe base**, e depois acrescenta ou altera os seus próprios.

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def describe(self):
        return self.name + " the animal"

class Dog(Animal):           # Dog IS an Animal
    def speak(self):
        return "Woof"
```

- `class Dog(Animal):` faz de `Dog` uma subclasse de `Animal`. Uma instância de
  `Dog` pode chamar `describe()` -- herdado de `Animal` -- *e* `speak()`, o seu
  próprio.
- A relação é "**é-um**": um `Dog` **é um** `Animal`, logo
  `isinstance(dog, Animal)` é `True`.
- O comportamento partilhado vive apenas uma vez na base; as subclasses não o
  repetem.

## A tua tarefa

Define uma classe base `Animal` com um `__init__(self, name)` e um
`describe(self)` que devolve `"<name> the animal"`. Depois define `Dog(Animal)`
que **herda** dela e acrescenta `speak(self)` que devolve `"Woof"`.

## Está feito quando

- `Dog("Rex").describe()` devolve `"Rex the animal"` (herdado).
- `Dog("Rex").speak()` devolve `"Woof"`.
- Um `Dog` **é um** `Animal`: herda em vez de copiar `describe`.
