**`Counter`** (do módulo **`collections`**) é uma subclasse de `dict` que
conta um iterável numa só chamada: `Counter(items)` devolve um mapeamento de
cada item distinto para quantas vezes aparece — o ciclo `counts.get(k, 0) +
1`, já escrito.

- Por ser um dict, suporta tudo o que um dict faz (`c[key]`, `c.items()`,
  `key in c`) e é **igual**, na comparação, a um dict simples com as mesmas
  contagens.
- Uma chave **em falta** lê-se como `0` em vez de gerar `KeyError`, o que é
  ideal para contar.
- **`c.most_common(n)`** devolve os `n` pares `(item, count)` com maior
  contagem, já ordenados — o passo do relatório de graça. Os Counters também
  somam e subtraem (`c1 + c2`) para combinar contagens.

```python
from collections import Counter

c = Counter("banana")     # Counter({'a': 3, 'n': 2, 'b': 1})
c["a"]                    # 3
c["z"]                    # 0  -- no KeyError
c.most_common(1)          # [('a', 3)]
```
