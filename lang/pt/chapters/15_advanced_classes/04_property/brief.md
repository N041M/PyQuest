# 15.4 -- @property: um atributo calculado

## Conceito

Por vezes um valor é **derivado** de outros -- a área de um retângulo a partir
da largura e da altura. Podias guardá-lo, mas depois fica desatualizado
quando a largura muda. Uma **`@property`** calcula-o em cada acesso,
continuando a ser lida como um simples atributo:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

r = Rectangle(3, 4)
r.area        # 12   -- no parentheses, but the method runs
r.width = 5
r.area        # 20   -- recomputed from the new width
```

- `@property` acima de um método faz com que `obj.area` (sem `()`) chame esse
  método e devolva o seu resultado.
- Como é executado de cada vez, o valor está sempre atualizado -- ao contrário
  de um valor guardado uma única vez no `__init__`.

## A tua tarefa

Define `Rectangle` com `__init__(self, width, height)` e uma **propriedade**
**`area`** que devolve `width * height`.

## Está feito quando

- `Rectangle(3, 4).area` é `12` (acedido sem parênteses).
- Depois de `r = Rectangle(3, 4); r.width = 5`, `r.area` é `20` -- recalculado,
  não guardado.
