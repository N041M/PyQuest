**`sum(numbers)`** soma um iterável de números e devolve o total — o
ciclo acumulador de 3.12 numa só chamada nativa.

- Funciona em qualquer iterável de números (lista, tuplo, range, gerador). `sum([])`
  é `0`.
- Um segundo argumento opcional é o valor **inicial**: `sum(nums, 100)` começa o
  total em 100.
- Só soma números; para totalizar algo derivado de cada item, alimenta-o com uma
  compreensão ou gerador, por exemplo `sum(len(w) for w in words)`.

```python
sum([3, 1, 4])              # 8
sum(range(1, 101))          # 5050
sum(len(w) for w in words)  # total characters
```
