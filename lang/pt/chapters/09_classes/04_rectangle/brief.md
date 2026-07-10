# 9.4 -- Mais dados, mais métodos

## Conceito

Uma classe pode guardar várias peças de dados e oferecer vários métodos sobre
elas. Nada de novo na sintaxe -- apenas mais dela:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
```

Os dois métodos leem os mesmos dados guardados através de `self`; cada
Rectangle responde a qualquer uma das duas perguntas sobre si próprio:

```python
r = Rectangle(3, 4)
r.area()        # 12
r.perimeter()   # 14
```

## A tua tarefa

Define uma classe `Rectangle` cujo `__init__` guarda um `width` e um `height`,
com dois métodos: `area()` devolve `width * height`, e `perimeter()` devolve
`2 * (width + height)`.

## Está feito quando

- `Rectangle(3, 4).area()` é `12` e `.perimeter()` é `14`.
- Ambos funcionam para qualquer largura e altura.
- Ambos são métodos na classe, calculando a partir de `self`.
