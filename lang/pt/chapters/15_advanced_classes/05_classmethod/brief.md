# 15.5 -- @classmethod: um construtor alternativo

## Conceito

Um método normal recebe `self` (uma instância). Um **`@classmethod`** recebe
**`cls`** (a própria classe), pelo que pode construir e devolver uma **nova
instância** -- uma forma prática de oferecer um construtor alternativo, com
nome:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_tuple(cls, pair):
        return cls(pair[0], pair[1])

p = Point.from_tuple((3, 4))     # called on the class, not an instance
p.x, p.y                          # (3, 4)
```

- `@classmethod` faz de `cls` o primeiro parâmetro -- a classe em que o
  método é chamado (`Point` aqui).
- `cls(...)` é o mesmo que `Point(...)`, mas usar `cls` significa que as
  subclasses recebem de graça uma instância do *seu próprio* tipo.
- Chama-se na **classe**: `Point.from_tuple(...)`.

## A tua tarefa

Define `Point` com `__init__(self, x, y)`, e um **classmethod**
`from_tuple(cls, pair)` que constrói um `Point` a partir de um tuplo `(x, y)`.

## Está feito quando

- `Point.from_tuple((3, 4)).x` é `3` e `.y` é `4`.
- `from_tuple` é um `@classmethod` que recebe `cls`, e constrói o ponto com
  `cls(...)`.
