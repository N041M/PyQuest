# 9.5 -- Imprimir um objeto: `__str__`

## Conceito

Imprime um objeto tal como está e obténs algo inútil como
`<__main__.Point object at 0x10f3d2b80>`. Para controlar o aspeto de um
objeto como texto, define o método especial `__str__`, que devolve a cadeia
de caracteres que o Python deve mostrar.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
```

`__str__` é um **dunder** (duplo sublinhado) -- o Python chama-o por ti sempre
que o objeto é transformado em texto, por `print()` ou `str()`:

```python
p = Point(3, 4)
print(p)        # (3, 4)
str(p)          # "(3, 4)"
```

Nunca chamas `__str__` diretamente; apenas o defines, e `str(p)` aciona-o.

## A tua tarefa

Define uma classe `Point` que guarda `x` e `y`, com um método `__str__` para
que `str(Point(3, 4))` seja exatamente `"(3, 4)"` -- os dois valores entre
parênteses, com vírgula e espaço entre eles.

## Está feito quando

- `str(Point(3, 4))` é `"(3, 4)"`.
- Funciona para qualquer `x` e `y`, incluindo negativos.
- A formatação vem de um método `__str__` na classe.
