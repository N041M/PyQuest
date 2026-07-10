**`map(func, iterable)`** aplica `func` a cada item e produz os resultados —
o padrão "transformar cada item" como função de ordem superior (uma que recebe
outra função como argumento).

- Devolve um **iterador preguiçoso**, calculando cada resultado à medida da
  necessidade; envolve-o em `list(...)` (ou `tuple`, ou alimenta um `for`) para
  o consumir.
- `func` pode ser uma `lambda`, um `def` com nome, ou qualquer chamável — uma
  função nativa como `len`, `str.upper`, ou `int` é comum.
- Dados vários iteráveis, `map(func, a, b)` chama `func(a_i, b_i)` em
  sincronia, parando no mais curto.
- Uma compreensão de lista `[func(x) for x in items]` exprime a mesma coisa e
  é muitas vezes mais clara; `map` é o equivalente em estilo funcional que vais
  ver com frequência.

```python
list(map(len, ["hi", "there"]))        # [2, 5]
list(map(lambda x: x * x, [1, 2, 3]))  # [1, 4, 9]
list(map(int, ["1", "2", "3"]))        # [1, 2, 3]
```
