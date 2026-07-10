# 16.2 -- Carrinho: guardar itens e somar o total

## Passo 2

Agora o **carrinho** em si. Constrói uma classe `Cart` que reúne itens por
nome e preço e soma a conta.

- `__init__(self)` inicia um carrinho vazio.
- `add(self, name, price)` adiciona um item ao carrinho.
- `total(self)` devolve a soma de todos os preços (0 para um carrinho vazio).

## Está feito quando

- Um novo `Cart()` tem `total()` igual a `0`.
- Depois de `add("Apple", 1.5)` e `add("Bread", 2.0)`, `total()` é `3.5`.
- `add` pode ser chamado qualquer número de vezes antes de `total`.
