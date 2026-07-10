**`__str__`** define o texto legível por humanos para um objeto. Quando fazes
`print` de uma instância ou chamas `str()` sobre ela, o Python chama `__str__`
e usa o que ele devolver.

- Sem ele, imprimir um objeto mostra um padrão pouco útil como
  `<Point object at 0x...>`; `__str__` substitui isso por algo com
  significado.
- Tem de **devolver** uma cadeia de caracteres (não imprimir uma),
  normalmente construída com uma f-string a partir dos atributos do objeto.
- `__str__` é um dos vários métodos **dunder** ("duplo sublinhado") que o
  Python chama em teu nome, como `__init__`.

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __str__(self):
        return f"({self.x}, {self.y})"

print(Point(3, 4))      # (3, 4)
```
