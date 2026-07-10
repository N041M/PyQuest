# 15.2 -- super(): estender o pai

## Conceito

Uma subclasse muitas vezes precisa de tudo o que o `__init__` do pai faz **e
mais** um pouco. **`super()`** dá-te acesso ao pai, para que possas chamar o
seu método e depois acrescentar-lhe algo -- em vez de copiares o código do
pai:

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)     # run Animal's __init__ (sets self.name)
        self.breed = breed         # then add Dog's own attribute
```

- `super().__init__(name)` chama o `__init__` do **pai** nesta instância, para
  que `self.name` seja definido por `Animal`.
- Depois disso, o filho acrescenta o que lhe é próprio (`self.breed`).
- Isto mantém a configuração do pai num único sítio; se `Animal.__init__`
  mudar, `Dog` recebe a mudança automaticamente.

## A tua tarefa

Define `Animal` com `__init__(self, name)` a guardar `self.name`. Depois
define `Dog(Animal)` cujo `__init__(self, name, breed)` chama
**`super().__init__(name)`** e depois guarda `self.breed`.

## Está feito quando

- `Dog("Rex", "Lab").name` é `"Rex"` (definido via `super().__init__`).
- `Dog("Rex", "Lab").breed` é `"Lab"`.
- Um `Dog` é um `Animal`, e o nome é definido pelo pai, não reatribuído à mão.
