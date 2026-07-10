A **herança** permite que uma classe se construa a partir de outra. Escrever
`class Child(Parent):` faz de `Child` uma **subclasse**: automaticamente tem
todos os métodos de `Parent`, e pode acrescentar novos ou substituir os
existentes.

- A relação é **"é-um"**: um `Dog(Animal)` *é um* `Animal`, logo
  `isinstance(dog, Animal)` é `True` e um `Dog` funciona em qualquer sítio onde
  se espera um `Animal`.
- O comportamento partilhado vive **uma só vez** na classe base; as subclasses
  herdam-no em vez de o copiarem, por isso uma correção no pai chega a todos os
  filhos.
- O Python encontra um método percorrendo o **MRO** (method resolution order,
  ordem de resolução de métodos): primeiro a classe da instância, depois as
  suas bases. `object` é a base implícita de todas as classes.

```python
class Animal:
    def __init__(self, name): self.name = name
    def describe(self): return self.name + " the animal"

class Dog(Animal):
    def speak(self): return "Woof"

d = Dog("Rex")
d.describe()              # 'Rex the animal'  -- inherited
isinstance(d, Animal)    # True
```
