Os operadores aritméticos são `+` (somar), `-` (subtrair), `*` (multiplicar),
`/` (dividir), `//` (divisão inteira), `%` (resto), e `**` (potência).

Seguem uma **precedência** (ordem das operações), da mais alta para a mais baixa:

1. `**`
2. `-` unário (negação)
3. `*`, `/`, `//`, `%`
4. `+`, `-`

Operadores com a mesma precedência são avaliados **da esquerda para a direita**, exceto `**`, que é
associativo à direita (`2 ** 3 ** 2` é `2 ** 9`). Os **parênteses** sobrepõem-se a
tudo isto — são avaliados primeiro.

```python
2 + 3 * 4      # 14   -- * before +
(2 + 3) * 4    # 20   -- parentheses first
-3 ** 2        # -9   -- ** before unary minus
```
