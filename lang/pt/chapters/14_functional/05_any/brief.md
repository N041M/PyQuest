# 14.5 -- any: há pelo menos um verdadeiro?

## Conceito

**`any(iterable)`** devolve `True` se **pelo menos um** item for verdadeiro,
`False` caso contrário. Alimentado com um gerador de testes, responde a
"*algum* item passa?":

```python
any(n < 0 for n in [1, 2, -3])     # True
any(n < 0 for n in [1, 2, 3])      # False
```

- Substitui o ciclo com uma bandeira (`found = False; for ...: if ...: found =
  True`) por uma única expressão.
- Tem **avaliação abreviada**: para e devolve `True` no primeiro item
  verdadeiro.
- `any([])` é `False` (nada passou).

O padrão é `any(<test> for <item> in <iterable>)` -- uma expressão geradora de
booleanos passada a `any`.

## Exemplo

```python
def has_blank(strings):
    return any(s == "" for s in strings)
```

## A tua tarefa

Usando **`any`**, define `has_negative(nums)` que devolve `True` se `nums`
contiver pelo menos um número negativo.

## Está feito quando

- `has_negative([1, 2, -3])` é `True`; `has_negative([1, 2, 3])` é `False`.
- `has_negative([])` é `False`.
- A resposta vem de `any(...)`, não de um ciclo escrito à mão com uma
  bandeira.
