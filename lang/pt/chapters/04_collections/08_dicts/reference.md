Um **dicionário** (`dict`) associa **chaves** a **valores**: `{"a": 1, "b": 2}`. É
a ferramenta para consultas pelo nome em vez de pela posição.

- **`d[key]`** lê o valor de uma chave; **`d[key] = value`** adiciona a chave (se
  for nova) ou atualiza-a (se já existir). As chaves são únicas — atribuir a uma
  chave existente sobrescreve-a.
- Ler uma chave **inexistente** com `d[key]` gera `KeyError` (ver `.get`, 4.10).
- As chaves têm de ser imutáveis (cadeias de caracteres, números, tuplos); os
  valores podem ser qualquer coisa. `len(d)` conta os pares; `key in d` testa a
  existência de uma chave.

```python
ages = {"Ada": 36}
ages["Ada"]          # 36
ages["Linus"] = 21   # add a new pair
```
