**JSON** (JavaScript Object Notation) je standardní **textový** formát pro
strukturovaná data a modul **`json`** převádí pythonovské hodnoty do něj a z něj.

- **`json.dumps(obj)`** („dump string“) serializuje pythonovský `dict`, `list`,
  `str`, číslo, `bool` nebo `None` do JSON řetězce. Klíče se stanou řetězci a
  pythonovské `True`/`False`/`None` se zapíšou jako JSON `true`/`false`/`null`.
- **`json.loads(text)`** („load string“) rozparsuje JSON řetězec zpět na pythonovské
  hodnoty. Oba jsou inverzní: `json.loads(json.dumps(x)) == x`.
- `dumps` bere možnosti — `indent=2` hezky odsadí, `sort_keys=True` seřadí klíče.
  Souborově orientované `json.dump(obj, f)` / `json.load(f)` zapisují a čtou objekt
  souboru přímo.
- Serializují se jen typy kompatibilní s JSON; `set` nebo vlastní objekt vyvolají
  `TypeError`, pokud `dumps` neřekneš, jak ho převést.

```python
import json

json.dumps({"name": "Ada", "ok": True})   # '{"name": "Ada", "ok": true}'
json.loads('[1, 2, 3]')                    # [1, 2, 3]
```
