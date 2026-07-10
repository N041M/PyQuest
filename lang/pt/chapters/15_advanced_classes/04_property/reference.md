**`@property`** é um decorador que transforma um método num **atributo
calculado, só de leitura**. `obj.area` (sem parênteses) executa o método e
devolve o seu resultado, pelo que um valor derivado é recalculado em cada
acesso e nunca fica desatualizado.

- Esconde o facto de haver trabalho a ser feito: quem chama usa `obj.area`,
  não `obj.area()`, exatamente como para um atributo guardado — mas o valor
  reflete sempre o estado atual.
- Uma `@property` simples é só de leitura; atribuir-lhe um valor levanta
  `AttributeError`. Acrescenta um `@area.setter` correspondente para permitir
  a atribuição com validação.
- Prefere uma propriedade a um valor guardado no `__init__` sempre que o valor
  *depende* de outros atributos que podem mudar.

```python
class Rectangle:
    def __init__(self, w, h): self.width, self.height = w, h
    @property
    def area(self): return self.width * self.height

r = Rectangle(3, 4)
r.area        # 12
r.width = 5
r.area        # 20  -- recomputed
```
