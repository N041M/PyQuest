Colocar **`yield` atrás de um `if`** filtra um fluxo à medida que corre: o
gerador emite apenas os itens que passam o teste e salta silenciosamente os
restantes — o equivalente preguiçoso da cláusula `if` de uma compreensão.

- `for x in source: if test(x): yield x` produz um fluxo filtrado sem
  construir qualquer lista intermédia.
- Por ser preguiçoso, compõe-se de forma limpa: um gerador de filtro pode
  alimentar outro gerador, cada um a tratar de uma etapa.

```python
def evens(nums):
    for n in nums:
        if n % 2 == 0:
            yield n         # only the evens make it out

list(evens(range(10)))      # [0, 2, 4, 6, 8]
```
