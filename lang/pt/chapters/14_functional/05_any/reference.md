**`any(iterable)`** devolve `True` assim que **um** item é verdadeiro, caso
contrário `False`. Recebendo um gerador de testes, responde a "algum item
passa?" numa única expressão, substituindo um ciclo que define uma bandeira.

- Tem **avaliação abreviada**: a avaliação para no primeiro item verdadeiro,
  por isso é eficiente e funciona em iteráveis infinitos/preguiçosos.
- `any([])` é `False` — não há nada que seja verdadeiro.
- O idioma é `any(<test> for <item> in <iterable>)`: uma expressão geradora de
  booleanos. (O seu parceiro `all` é o 14.6.)

```python
any(n < 0 for n in [1, 2, -3])    # True
any(c.isdigit() for c in "abc")   # False
any([])                           # False
```
