# 16.3 -- Depuração: o desconto está errado

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
