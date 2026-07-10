**`filter(pred, iterable)`** mantém os itens para os quais o **predicado**
`pred` (uma função que devolve verdadeiro ou falso) é verdadeiro, descartando o
resto — a contrapartida "mantém se" do "transforma cada" de `map`.

- Devolve um **iterador preguiçoso** pela ordem original; envolve-o em
  `list(...)` para recolher.
- `pred` é qualquer chamável que devolva um valor verdadeiro/falso — uma
  `lambda`, um `def`, ou uma função nativa. Passar **`None`** como predicado
  (`filter(None, items)`) mantém os itens que são, eles próprios, verdadeiros,
  descartando `0`, `""`, `None`, etc.
- A compreensão `[x for x in items if pred(x)]` é o equivalente e muitas
  vezes lê-se melhor; `filter` é a forma funcional.

```python
list(filter(lambda x: x > 0, [-1, 2, -3, 4]))   # [2, 4]
list(filter(None, [0, 1, "", "a", None]))        # [1, 'a']
list(filter(str.isalpha, "a1b2"))                # ['a', 'b']
```
