# PyQuest translations -- language 'pt' -- chapter 16_project_cart -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply pt

TRANSLATIONS = {

"16.1 brief": r"""# 16.1 -- Item: uma coisa com um preço

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
""",

"16.1 hints": r"""Guarda `name` e `price` em `__init__`, depois escreve `label` para devolver a
cadeia de caracteres formatada.

---

Uma f-string com uma especificação de formato trata das duas casas decimais:
`f"{self.name}: ${self.price:.2f}"`.
""",

"16.2 brief": r"""# 16.2 -- Carrinho: guardar itens e somar o total

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
""",

"16.2 hints": r"""Mantém uma lista no carrinho (`self.items = []` em `__init__`); `add`
acrescenta-lhe itens.

---

`total` soma os preços -- `sum(price for name, price in self.items)` se
guardares pares `(name, price)`.
""",

"16.3 brief": r"""# 16.3 -- Depuração: o desconto está errado

## Passo 3 -- corrige o erro

Desta vez o código **já está escrito** -- e tem um erro. Um `Cart` com um
método `discounted_total(percent)` deve retirar `percent` **por cento** do
total. Mas os clientes estão a relatar que o desconto é exageradamente
grande: um cupão de 10% num carrinho de \$50 está a cobrar \$40 em vez de
\$45.

Abre a área de trabalho, lê `discounted_total`, percebe o que ele está
realmente a fazer, e corrige-o. Deixa o resto da classe em paz.

## Está feito quando

- `discounted_total(0)` é igual ao `total()` completo (sem desconto).
- Um desconto de 10% num carrinho de \$50 dá `45.0`, não `40.0`.
- Para qualquer total `t` e percentagem `p`, `discounted_total(p)` é
  `t * (1 - p/100)`.
""",

"16.3 hints": r"""Um desconto percentual escala o total -- não subtrai um valor fixo.
Manter `p`% de `100%` significa multiplicar por `(1 - p/100)`.
""",

"16.4 brief": r"""# 16.4 -- Culminação: imprime o recibo

## Passo 4 -- o fim, por conta própria

Desta vez sem tutorial passo a passo. Junta as peças.

Escreve uma função `receipt(items)` em que `items` é uma lista de pares
`(name, price)`. Devolve uma cadeia de caracteres com várias linhas: **uma
linha por item** no formato `"name: $price"` (duas casas decimais), seguida
de uma última linha **`"TOTAL: $<total>"`**.

Para `receipt([("Apple", 1.5), ("Bread", 2.0)])`:

```
Apple: $1.50
Bread: $2.00
TOTAL: $3.50
```

## Está feito quando

- Cada item é a sua própria linha, formatada `"name: $price"` com duas casas
  decimais.
- A última linha é `"TOTAL: $<sum of prices>"`, também com duas casas
  decimais.
- Uma lista vazia devolve apenas `"TOTAL: $0.00"`.
""",
}
