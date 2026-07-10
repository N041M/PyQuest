Uma função devolve **um** objeto, mas esse objeto pode ser um **tuplo**, por isso
`return a, b` devolve vários valores de uma vez (o Python empacota-os num tuplo).
Quem chama **desempacota**-os com nomes correspondentes.

- `return lo, hi` devolve o tuplo `(lo, hi)`; `low, high = bounds(xs)` desempacota-o
  em dois nomes.
- As contagens têm de corresponder no desempacotamento. Podes capturar o tuplo inteiro com um só nome se
  preferires: `result = bounds(xs)` depois `result[0]`, `result[1]`.

```python
def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max([3, 1, 4])   # lo = 1, hi = 4
```
