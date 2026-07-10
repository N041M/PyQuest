O capstone junta o capítulo todo numa única hierarquia, tal como as classes
reais são construídas:

- **Herança** — `Rectangle(Shape)` *é um* `Shape`, por isso recebe `describe`
  de graça e `isinstance(r, Shape)` é verdadeiro.
- **`super()`** — `Rectangle.__init__` chama `super().__init__("rectangle")`
  para deixar a base definir `self.name`, e depois acrescenta a sua própria
  largura e altura.
- **`@property`** — `area` é calculada a partir da largura e da altura em
  cada acesso, por isso mantém-se correta quando um lado muda.
- **Polimorfismo** — `Shape.describe` lê `self.area`, que só `Rectangle`
  define; o método da base funciona através da propriedade da subclasse.
- **Dunders** — `__eq__` e `__lt__` (ambos por área) fazem com que os
  retângulos se comparem e ordenem como valores nativos, por isso `==` e
  `sorted` simplesmente funcionam.

Juntas, estas peças transformam um objeto simples num que se comporta como um
valor de primeira classe: tem uma identidade numa hierarquia, dados
derivados, e igualdade e ordenação com significado — o resultado de todo o
capítulo.

```python
r = Rectangle(3, 4)
r.describe()                              # 'rectangle with area 12'
Rectangle(2, 6) == Rectangle(3, 4)        # True  -- equal areas
sorted([Rectangle(3, 4), Rectangle(1, 1)])   # by area: 1, then 12
```
