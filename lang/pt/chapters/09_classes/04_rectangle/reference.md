Uma classe pode guardar **vários atributos** e oferecer **vários métodos**
que trabalham em conjunto sobre eles — modelando algo com mais do que uma
propriedade.

- `__init__` guarda cada peça de dados (`self.width`, `self.height`); cada
  método lê os atributos de que precisa.
- Os métodos podem basear-se nos mesmos dados para respostas diferentes:
  `area` multiplica, `perimeter` soma — um objeto, muitas perguntas.
- Manter os dados e as operações numa só classe significa que quem chama
  pergunta ao objeto em vez de andar a gerir variáveis soltas.

```python
class Rectangle:
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):      return self.w * self.h
    def perimeter(self): return 2 * (self.w + self.h)

r = Rectangle(3, 4); r.area(), r.perimeter()   # (12, 14)
```
