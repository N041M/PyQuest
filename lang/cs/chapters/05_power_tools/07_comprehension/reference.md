**Seznamová komprehenze** sestaví nový seznam jediným výrazem: pro každé `x` v
`items` vyhodnotí `expr` a posbírá výsledky, v pořadí. Je to vzor „stav cyklem a
append“ stlačený do jednoho řádku.

- `[expr for x in items]` je ekvivalentní tomu, že začneš `result = []` a v cyklu
  `result.append(expr)` — stejný výsledek, přímější.
- `expr` může být libovolný výraz v `x`: `[n * n for n in nums]`,
  `[w.upper() for w in words]`.
- Komprehenze staví i množiny (`{...}`) a slovníky (`{k: v for ...}`).

```python
[n * n for n in range(5)]       # [0, 1, 4, 9, 16]
[w.upper() for w in ["a", "b"]] # ['A', 'B']
```
