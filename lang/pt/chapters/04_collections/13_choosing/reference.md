As três coleções principais servem para tarefas diferentes — escolher a certa
torna o código mais simples e mais rápido:

- **lista** — uma sequência **ordenada** que pode repetir valores. Usa-a para
  guardar todos os valores, por ordem (um registo, uma fila de itens a processar).
- **conjunto** — um grupo não ordenado de itens **distintos** com pertença rápida.
  Usa-o para descartar duplicados ou perguntar "já vi isto?".
- **dicionário** — um mapeamento de **chaves para valores**. Usa-o para procurar
  algo pelo nome (uma contagem por palavra, um preço por item).

Pergunta: preciso de ordem e repetições (lista), unicidade e pertença (conjunto),
ou consulta por chave (dicionário)?

```python
order  = ["a", "b", "a"]    # keep all, in order
unique = {"a", "b"}         # distinct only
price  = {"a": 2, "b": 5}   # look up by key
```
