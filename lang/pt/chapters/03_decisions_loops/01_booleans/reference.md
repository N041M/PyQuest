Um **booleano** é um de dois valores, `True` ou `False` (tipo `bool`). Os
**operadores de comparação** produzem um booleano ao comparar dois valores:

- `==` igual, `!=` diferente,
- `<` menor que, `>` maior que, `<=` no máximo, `>=` no mínimo.

`==` (uma pergunta, "isto é igual?") não é `=` (um comando, "atribuir"). Os números
comparam-se por valor; as strings comparam-se **lexicograficamente** (ordem
alfabética, por código de carácter, pelo que as maiúsculas ficam antes das
minúsculas). As comparações podem ser **encadeadas**: `0 <= x < 10` significa
`0 <= x and x < 10`.

```python
3 < 5        # True
3 == 3.0     # True   -- valores iguais, tipos diferentes
"a" < "b"    # True
```
