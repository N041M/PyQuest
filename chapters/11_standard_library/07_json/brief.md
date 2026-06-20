# 11.7 -- json: data as text

## Concept

To save data to a file or send it over a network, you need it as **text**.
**JSON** is the near-universal text format for structured data, and the **`json`**
module converts both ways:

```python
import json

json.dumps({"name": "Ada", "score": 90})   # '{"name": "Ada", "score": 90}'
json.loads('{"ok": true}')                  # {'ok': True}
```

- `json.dumps(obj)` -- "dump string" -- turns a Python dict/list/number/str into
  a JSON **string**.
- `json.loads(text)` -- "load string" -- parses a JSON string back into Python
  values.
- The two are inverses: `json.loads(json.dumps(x))` gives `x` back.

Note JSON's spelling differs slightly from Python's (`true`/`false`/`null`), which
is exactly why you let the module handle it instead of formatting by hand.

## Example

```python
import json

def parse(text):
    return json.loads(text)
```

## Your task

Using **`json.dumps`**, define `to_json(record)` that returns the JSON string
for the dictionary `record`.

## Done when

- `to_json({"a": 1, "b": 2})` returns `'{"a": 1, "b": 2}'`.
- `to_json({})` returns `'{}'`.
- The string is produced by `json.dumps`, not built by hand.
