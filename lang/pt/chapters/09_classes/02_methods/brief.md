# 9.2 -- Métodos: comportamento sobre os dados

## Conceito

Os objetos não guardam apenas dados -- têm **métodos**, funções que vivem no
objeto e trabalham com os seus próprios dados através de `self`.

```python
class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
```

`area` é um método: recebe `self` (o objeto sobre o qual é chamado) e usa
`self.side`. Chama-lo com um ponto e parênteses -- não precisas de passar
`self`, o Python trata disso:

```python
s = Square(5)
print(s.area())   # 25
```

O objetivo de um método é que o comportamento viaja *com* os dados: qualquer
Square já sabe como calcular a sua própria área.

## A tua tarefa

Define uma classe `Square` cujo `__init__` guarda um `side`, e acrescenta um
método `area()` que devolve a área do quadrado (`side * side`).

## Está feito quando

- `Square(5).area()` devolve `25`.
- Funciona para qualquer comprimento de lado, incluindo `0`.
- `area` é um método na classe e calcula a partir de `self.side`.
