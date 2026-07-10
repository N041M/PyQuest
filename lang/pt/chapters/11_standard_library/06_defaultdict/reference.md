**`defaultdict`** (de **`collections`**) é um `dict` que fornece
automaticamente um valor por omissão para uma chave em falta. Passas-lhe uma
**factory** — um callable sem argumentos que constrói o valor por omissão —
e, na primeira vez que lês ou tocas numa chave ausente, ele chama a factory,
guarda o resultado e usa-o.

- `defaultdict(list)` cria um `[]` novo para cada chave nova, por isso
  `d[k].append(x)` funciona sem qualquer preparação "if key not in d" — o
  idioma de agrupamento.
- `defaultdict(int)` cria `0` para cada chave nova, por isso `d[k] += 1`
  conta.
- Só a **procura** de uma chave em falta desencadeia a factory; de resto é um
  dict normal. `dict(d)` converte para um dict simples, e uma chave
  *verdadeiramente* em falta continua a ler-se como o valor por omissão em
  vez de gerar um erro.

```python
from collections import defaultdict

groups = defaultdict(list)
groups[5].append("hello")    # key 5 auto-starts as []
groups                       # defaultdict(<class 'list'>, {5: ['hello']})
```
