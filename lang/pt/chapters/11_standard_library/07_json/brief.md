# 11.7 -- json: dados como texto

## Conceito

Para guardar dados num ficheiro ou enviá-los pela rede, precisas deles como
**texto**. O **JSON** é o formato de texto quase universal para dados
estruturados, e o módulo **`json`** converte nos dois sentidos:

```python
import json

json.dumps({"name": "Ada", "score": 90})   # '{"name": "Ada", "score": 90}'
json.loads('{"ok": true}')                  # {'ok': True}
```

- `json.dumps(obj)` -- "dump string" -- transforma um dict/list/número/str
  do Python numa **string** JSON.
- `json.loads(text)` -- "load string" -- interpreta uma string JSON de volta
  para valores Python.
- As duas são inversas: `json.loads(json.dumps(x))` devolve `x` de novo.

Repara que a grafia do JSON difere ligeiramente da do Python
(`true`/`false`/`null`), o que é exatamente a razão para deixares o módulo
tratar disso em vez de formatares à mão.

## Exemplo

```python
import json

def parse(text):
    return json.loads(text)
```

## A tua tarefa

Usando **`json.dumps`**, define `to_json(record)` que devolve a string
JSON do dicionário `record`.

## Está feito quando

- `to_json({"a": 1, "b": 2})` devolve `'{"a": 1, "b": 2}'`.
- `to_json({})` devolve `'{}'`.
- A string é produzida por `json.dumps`, não construída à mão.
