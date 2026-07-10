# 6.7 -- Construir sobre funções nativas

## Conceito

As funções brilham quando embrulham uma pequena *receita* atrás de um bom nome. A
receita de uma média:

> o total, dividido pela quantidade de itens

Tens todos os ingredientes: `sum()` (5.2), `len()` (2.6), e `/` (1.9).
Lembra-te de 1.9 que `/` **devolve sempre um float** -- `4 / 2` é `2.0`,
não `2`. Isso está correto aqui: uma média é naturalmente um número decimal.

```python
def average(nums):
    return sum(nums) / len(nums)
```

Uma função, uma linha, instantaneamente reutilizável -- e o nome diz o que a linha
significa.

## Exemplo

```python
average([1, 2])        # 1.5
average([10, 20, 30])  # 20.0
```

## A tua tarefa

Define `average(nums)` que devolva a média de uma lista não vazia de
números.

## Está feito quando

- `average([1, 2])` devolve `1.5`; `average([10, 20, 30])` devolve `20.0`.
- O resultado é um **float** mesmo quando a divisão é exata (usa `/`,
  não `//`).
- Uma lista com um só item devolve esse item (como float).
