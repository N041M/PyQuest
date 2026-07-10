**`all(iterable)`** devolve `True` apenas se **todos** os itens forem
verdadeiros — o parceiro de `any`. Responde a "passam todos?" numa única
expressão.

- Tem **avaliação abreviada** no primeiro item falso, devolvendo `False`
  imediatamente.
- `all([])` é `True` — *vacuamente*, já que nenhum item falhou. Esta regra de
  "todos de nada é verdadeiro" é uma surpresa comum; protege-te contra o caso
  vazio se isso importar.
- Mesma forma que `any`: `all(<test> for <item> in <iterable>)`. Juntos,
  exprimem as questões universal ("para todos") e existencial ("existe") sobre
  uma sequência.

```python
all(n > 0 for n in [1, 2, 3])     # True
all(n > 0 for n in [1, -2, 3])    # False
all([])                           # True  -- vacuously
```
