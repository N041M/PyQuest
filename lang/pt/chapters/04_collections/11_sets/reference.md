Um **conjunto** é uma coleção não ordenada de itens **únicos**: `{1, 2, 3}`.
Modela "um grupo de coisas distintas" e testa a pertença rapidamente.

- Construir um conjunto a partir de uma sequência **descarta duplicados**:
  `set([1, 1, 2])` é `{1, 2}`. O conjunto vazio é `set()` — `{}` é um *dicionário*
  vazio.
- **`x in s`** testa a pertença e é muito mais rápido do que percorrer uma lista,
  porque os conjuntos são baseados em hash.
- Os conjuntos não são ordenados (sem indexação, sem slicing) e só contêm itens
  imutáveis. Adiciona com `.add(x)`, remove com `.discard(x)`.

```python
seen = set()
seen.add("a"); seen.add("a")   # {'a'} -- duplicate ignored
"a" in seen                    # True
set([3, 1, 3, 2])              # {1, 2, 3}
```
