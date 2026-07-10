# 6.6 -- Devolver dois valores

## Conceito

`return` pode devolver **vários valores de uma vez** -- separa-os com uma
vírgula e o Python empacota-os num **tuplo** (4.7):

```python
def min_max(nums):
    return min(nums), max(nums)
```

Quem chama pode guardar o tuplo, ou desempacotá-lo diretamente em variáveis -- o
mesmo desempacotamento que usaste em `a, b = b, a`:

```python
pair = min_max([3, 1, 4])     # (1, 4)  -- one tuple
lo, hi = min_max([3, 1, 4])   # lo = 1, hi = 4  -- unpacked
```

É assim que as funções em Python devolvem "duas respostas" -- não há nenhum
truque especial, apenas um tuplo e desempacotamento.

## Exemplo

```python
def split_name(full):
    parts = full.split()
    return parts[0], parts[-1]

first, last = split_name("Ada King Lovelace")
# first = "Ada", last = "Lovelace"
```

## A tua tarefa

Define `min_max(nums)` que devolva o item mais pequeno e o maior de uma
lista não vazia, **por essa ordem**, como um tuplo. (`min()`/`max()` são de 5.3.)

## Está feito quando

- `min_max([3, 1, 4])` devolve `(1, 4)` -- um tuplo, o mais pequeno primeiro.
- `min_max([7])` devolve `(7, 7)`.
- Números negativos funcionam.
