**JSON** (JavaScript Object Notation) is the standard **text** format for
structured data, and the **`json`** module converts Python values to and from it.

- **`json.dumps(obj)`** ("dump string") serializes a Python `dict`, `list`,
  `str`, number, `bool`, or `None` into a JSON string. Keys become strings, and
  Python's `True`/`False`/`None` are written as JSON's `true`/`false`/`null`.
- **`json.loads(text)`** ("load string") parses a JSON string back into Python
  values. The two are inverses: `json.loads(json.dumps(x)) == x`.
- `dumps` takes options — `indent=2` pretty-prints, `sort_keys=True` orders the
  keys. The file-oriented `json.dump(obj, f)` / `json.load(f)` write and read a
  file object directly.
- Only JSON-compatible types serialize; a `set` or a custom object raises
  `TypeError` unless you tell `dumps` how to convert it.

```python
import json

json.dumps({"name": "Ada", "ok": True})   # '{"name": "Ada", "ok": true}'
json.loads('[1, 2, 3]')                    # [1, 2, 3]
```
