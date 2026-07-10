# 14.6 -- all: são todos verdadeiros?

## Conceito

**`all(iterable)`** é o parceiro de `any`: devolve `True` apenas se **todos**
os itens forem verdadeiros. Responde a "passam *todos*?":

```python
all(n > 0 for n in [1, 2, 3])      # True
all(n > 0 for n in [1, -2, 3])     # False
```

- Tem **avaliação abreviada** no sentido oposto: para e devolve `False` no
  primeiro item que falha.
- `all([])` é `True` -- vacuamente, já que nenhum item falhou. (Uma surpresa
  comum: "todos de nada" é verdadeiro.)

Mesma forma que `any`: `all(<test> for <item> in <iterable>)`.

## Exemplo

```python
def all_words(strings):
    return all(s.isalpha() for s in strings)
```

## A tua tarefa

Usando **`all`**, define `all_positive(nums)` que devolve `True` se **todos**
os números em `nums` forem maiores que zero.

## Está feito quando

- `all_positive([1, 2, 3])` é `True`; `all_positive([1, -2, 3])` é `False`.
- `all_positive([])` é `True` (nada falha).
- A resposta vem de `all(...)`, não de um ciclo escrito à mão com uma
  bandeira.
