# 3.4 -- elif

## Conceito

O `elif` (abreviatura de "else if") acrescenta **mais ramos** entre o `if` e o `else`.
O Python verifica cada condição por ordem e executa a **primeira** que for `True`;
as restantes são ignoradas. O `else` (opcional) apanha tudo o que sobrar.

```python
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
```

A ordem importa: como o primeiro ramo verdadeiro é o que vence, normalmente vais da
condição mais específica ou mais elevada para baixo.

## Exemplo

```python
n = 0
if n < 0:
    print("negative")
elif n == 0:
    print("zero")
else:
    print("positive")
# prints: zero
```

## A tua tarefa

Lê um número inteiro e imprime exatamente um destes:

- `negative` se for menor que 0,
- `zero` se for 0,
- `positive` se for maior que 0.

Para a entrada `0` a saída é:

```
zero
```

## Está feito quando

- `-3` imprime `negative`, `0` imprime `zero`, `5` imprime `positive`.
- Exatamente uma linha é impressa para qualquer entrada.
