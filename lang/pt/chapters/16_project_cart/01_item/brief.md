# 16.1 -- Item: uma coisa com um preço

## Projeto: Carrinho de Compras

Este capítulo é um **projeto**. Ao longo de quatro passos vais construir um
pequeno carrinho de compras e depois montá-lo com pouca ajuda. As lições ficam
para trás agora -- aqui vais pô-las em prática.

## Passo 1

Toda a loja precisa de **itens**. Constrói uma classe `Item`.

- `__init__(self, name, price)` guarda o nome e o preço.
- `label(self)` devolve o item como uma cadeia de caracteres `"name: $price"`,
  com o preço com **duas casas decimais** -- por exemplo, `"Apple: $1.50"`.

## Está feito quando

- `Item("Apple", 1.5).name` é `"Apple"` e `.price` é `1.5`.
- `Item("Apple", 1.5).label()` é `"Apple: $1.50"`.
- `Item("Bread", 2).label()` é `"Bread: $2.00"`.
