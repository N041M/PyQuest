**Sobrepor** é definir, numa subclasse, um método que o pai já tem. Para as
instâncias da subclasse, o Python encontra primeiro a versão da subclasse
(está mais acima no MRO), pelo que o comportamento do filho substitui o do
pai.

- Isto é **polimorfismo**: um único ponto de chamada, `x.speak()`, executa o
  código certo para o tipo que `x` realmente é — `Cat` diz "Meow", um `Animal`
  genérico diz "...". O código que chama não precisa de saber o tipo exato.
- A subclasse continua a **herdar** tudo o que *não* sobrepõe (aqui,
  `__init__`).
- Uma sobreposição pode reutilizar a versão do pai com `super().method()` —
  estender em vez de substituir por completo.

```python
class Animal:
    def speak(self): return "..."
class Cat(Animal):
    def speak(self): return "Meow"

for a in [Animal(), Cat()]:
    print(a.speak())     # '...' then 'Meow' -- same call, different result
```
