# 6.2 -- Dois parâmetros

## Conceito

Uma função pode receber vários parâmetros -- lista-os com vírgulas, e os
valores de quem chama chegam **pela mesma ordem**:

```python
def rect_area(width, height):
    return width * height

rect_area(3, 4)     # 12  (width=3, height=4)
```

Dentro do corpo, os parâmetros são variáveis normais. Tudo o que já sabes
funciona com eles -- aritmética, comparações, f-strings, ciclos.

Uma subtileza que vale a pena conhecer cedo: os parâmetros são **locais** à função. O
`width` dentro de `rect_area` só existe enquanto uma chamada está a correr; não é
visível (e não entra em conflito com) nada fora dela.

## Exemplo

```python
def diff(a, b):
    return a - b

print(diff(10, 4))   # 6
print(diff(4, 10))   # -6  -- order matters
```

## A tua tarefa

Define `rect_area(width, height)` que devolva a área de um retângulo
(largura vezes altura).

## Está feito quando

- `rect_area(3, 4)` devolve `12`; `rect_area(4, 3)` também.
- Um lado zero devolve `0`.
- Sem `input()`, sem `print()` -- o verificador passa os valores diretamente.
