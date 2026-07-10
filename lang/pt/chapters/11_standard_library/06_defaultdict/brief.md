# 11.6 -- defaultdict: um valor por omissão para chaves em falta

## Conceito

Para agrupar itens num dict simples, primeiro tens de verificar se a chave
existe:

```python
if length not in groups:
    groups[length] = []
groups[length].append(word)
```

O **`defaultdict`** remove essa cerimónia. Dás-lhe uma **factory** -- uma
função que cria o valor por omissão -- e ele chama a factory automaticamente
na primeira vez que tocas numa chave em falta:

```python
from collections import defaultdict

groups = defaultdict(list)     # missing key -> a fresh []
groups[5].append("hello")      # no setup needed
```

- `defaultdict(list)` cria uma lista vazia para qualquer chave nova, por
  isso o `.append` funciona sem mais.
- `defaultdict(int)` cria `0` para qualquer chave nova -- uma contagem sem
  `.get`.
- De resto é um dict a sério; converte com `dict(groups)` se quiseres um
  simples.

## Exemplo

```python
from collections import defaultdict

def by_first_letter(words):
    groups = defaultdict(list)
    for w in words:
        groups[w[0]].append(w)
    return dict(groups)
```

## A tua tarefa

Usando **`defaultdict`** de `collections`, define `group_by_length(words)`
que devolve um dict que mapeia cada **comprimento** de palavra à lista de
palavras desse comprimento, pela ordem original.

## Está feito quando

- `group_by_length(["hi", "ok", "bye"])` é igual a `{2: ["hi", "ok"], 3: ["bye"]}`.
- `group_by_length([])` é igual a `{}`.
- O agrupamento usa um `defaultdict(list)`, não uma verificação manual "if key in dict".
