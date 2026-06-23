# 11.7 -- json: data jako text

## Koncept

Abys uložil data do souboru nebo je poslal přes síť, potřebuješ je jako **text**.
**JSON** je téměř univerzální textový formát pro strukturovaná data a modul **`json`**
převádí oběma směry:

```python
import json

json.dumps({"name": "Ada", "score": 90})   # '{"name": "Ada", "score": 90}'
json.loads('{"ok": true}')                  # {'ok': True}
```

- `json.dumps(obj)` -- „dump string“ -- promění pythonovský dict/list/číslo/str na
  JSON **řetězec**.
- `json.loads(text)` -- „load string“ -- rozparsuje JSON řetězec zpět na pythonovské
  hodnoty.
- Oba jsou inverzní: `json.loads(json.dumps(x))` vrátí `x`.

Všimni si, že JSON se píše mírně jinak než Python (`true`/`false`/`null`), což je
přesně důvod, proč to necháš na modulu, místo abys formátoval ručně.

## Příklad

```python
import json

def parse(text):
    return json.loads(text)
```

## Tvůj úkol

Pomocí **`json.dumps`** definuj `to_json(record)`, která vrátí JSON řetězec pro
slovník `record`.

## Hotovo, když

- `to_json({"a": 1, "b": 2})` vrátí `'{"a": 1, "b": 2}'`.
- `to_json({})` vrátí `'{}'`.
- Řetězec produkuje `json.dumps`, ne ruční stavění.
