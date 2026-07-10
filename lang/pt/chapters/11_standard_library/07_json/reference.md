O **JSON** (JavaScript Object Notation) é o formato **texto** padrão para
dados estruturados, e o módulo **`json`** converte valores Python de e para
ele.

- **`json.dumps(obj)`** ("dump string") serializa um `dict`, `list`, `str`,
  número, `bool` ou `None` do Python numa string JSON. As chaves tornam-se
  strings, e o `True`/`False`/`None` do Python é escrito como o
  `true`/`false`/`null` do JSON.
- **`json.loads(text)`** ("load string") interpreta uma string JSON de volta
  para valores Python. As duas são inversas: `json.loads(json.dumps(x)) == x`.
- `dumps` aceita opções — `indent=2` formata de forma legível, `sort_keys=True`
  ordena as chaves. As versões orientadas a ficheiro `json.dump(obj, f)` /
  `json.load(f)` escrevem e leem diretamente um objeto de ficheiro.
- Só os tipos compatíveis com JSON são serializados; um `set` ou um objeto
  personalizado gera `TypeError` a menos que digas ao `dumps` como o
  converter.

```python
import json

json.dumps({"name": "Ada", "ok": True})   # '{"name": "Ada", "ok": true}'
json.loads('[1, 2, 3]')                    # [1, 2, 3]
```
