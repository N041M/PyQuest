# 16.4 -- Culminação: imprime o recibo

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
