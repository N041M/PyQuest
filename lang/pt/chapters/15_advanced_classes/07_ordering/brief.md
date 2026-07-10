# 15.7 -- __lt__: tornar objetos ordenáveis

## Conceito

`sorted`, `min` e `max` ordenam tudo usando o operador **`<`**. Por omissão,
o Python não sabe comparar dois dos teus objetos -- ordená-los levanta
`TypeError`. Define **`__lt__`** ("less than", menor que) e tornam-se
ordenáveis:

```python
class Temperature:
    def __init__(self, degrees):
        self.degrees = degrees
    def __lt__(self, other):
        return self.degrees < other.degrees

temps = [Temperature(30), Temperature(10), Temperature(20)]
sorted(temps)        # ordered 10, 20, 30 -- by degrees
```

- O Python chama `a.__lt__(b)` para `a < b`. Devolve se `a` deve vir
  **antes** de `b` -- normalmente comparando o atributo pelo qual queres
  ordenar.
- `sorted` só precisa de `<`, por isso só `__lt__` já torna uma lista dos teus
  objetos ordenável.

## A tua tarefa

Define `Temperature` com `__init__(self, degrees)` e um **`__lt__`** para que
as temperaturas se comparem por `degrees`.

## Está feito quando

- `Temperature(10) < Temperature(20)` é `True`.
- `sorted([Temperature(30), Temperature(10), Temperature(20)])` fica ordenado
  `10, 20, 30` por degrees.
- A comparação usa `degrees`.
