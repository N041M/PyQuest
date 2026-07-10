# 9.7 -- Objetos a trabalhar em conjunto

## Conceito

Um método pode receber **outro objeto** como argumento e construir um **novo**
objeto como resultado. É assim que os objetos se combinam sem perder a sua
própria identidade.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)
```

`add` vai buscar dados a `other` (outro Vector), e **devolve um `Vector` novo
em folha** -- não altera `self` nem `other`:

```python
a = Vector(1, 2)
b = Vector(3, 4)
c = a.add(b)      # Vector(4, 6)
a.x               # still 1 -- a is untouched
```

Construir um `Vector(...)` *dentro* do próprio método de `Vector` é normal: a
classe pode usar-se a si própria.

## A tua tarefa

Define uma classe `Vector` que guarda `x` e `y`, com um método `add(other)`
que devolve um **novo** `Vector` cujas coordenadas são a soma das coordenadas
dos dois vetores. Os originais têm de ficar inalterados.

## Está feito quando

- `Vector(1, 2).add(Vector(3, 4))` é um Vector com `.x == 4` e `.y == 6`.
- Os dois vetores de entrada ficam inalterados depois.
- `add` devolve um novo objeto `Vector` (não um tuplo), construído dentro do
  método.
