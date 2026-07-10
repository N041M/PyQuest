Um **`return`** simples dentro de um gerador — ou simplesmente chegar ao fim
da função — **para-o**: a iteração termina e não chegam mais valores.
`return` num gerador não transporta **nenhum valor**; apenas assinala
"terminado".

- Isto permite que um gerador **pare mais cedo** por uma condição:
  `if x == sentinela: return` termina o fluxo nesse ponto.
- Para um ciclo `for`, um gerador parado é apenas um iterável que se
  esgotou — o ciclo termina naturalmente (internamente, o gerador levanta
  `StopIteration`).

```python
def until_zero(nums):
    for n in nums:
        if n == 0:
            return          # stop the stream here
        yield n

list(until_zero([3, 1, 0, 9]))  # [3, 1]
```
