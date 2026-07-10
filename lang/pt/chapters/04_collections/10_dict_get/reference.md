**`d.get(key, default)`** procura uma chave de forma segura: devolve o valor se a
chave existir, caso contrário o `default` — sem gerar um erro. Sem valor por
omissão, devolve `None` para uma chave inexistente.

- Usa-o em vez de `d[key]` sempre que uma chave inexistente for um caso normal e
  esperado, e não um erro.
- É a base do idioma de **contagem**: `counts[k] = counts.get(k, 0) + 1` lê a
  contagem corrente (0 na primeira vez) e escreve a nova.
- `.get` só lê; nunca insere a chave (ao contrário de `setdefault`).

```python
ages = {"Ada": 36}
ages.get("Ada", 0)     # 36
ages.get("Nobody", 0)  # 0  -- no KeyError
```
