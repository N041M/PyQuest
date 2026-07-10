**`super()`** devolve um proxy para a **classe pai**, para que uma subclasse
possa chamar o método do pai e construir a partir dele em vez de duplicar o
seu código. O caso habitual é o `__init__`:

- `super().__init__(args)` executa o inicializador do pai nesta instância,
  configurando tudo o que o pai possui; o filho acrescenta depois os seus
  próprios atributos.
- Mantém a lógica do pai num **único sítio** — muda `Animal.__init__` e todas
  as subclasses que chamam `super().__init__` herdam a mudança.
- `super()` funciona para qualquer método, não só `__init__`: um método que
  sobrepõe pode chamar `super().method()` para reutilizar a versão do pai e
  estendê-la.
- Sem `super().__init__`, o inicializador do pai **não** é executado, pelo que
  os atributos que ele definiria ficam em falta.

```python
class Animal:
    def __init__(self, name): self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)     # Animal sets self.name
        self.breed = breed         # Dog adds self.breed

Dog("Rex", "Lab").name             # 'Rex'
```
