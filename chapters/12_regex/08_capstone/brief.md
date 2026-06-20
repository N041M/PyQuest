# 12.8 -- Capstone: parse key=value config

## Concept

Time to combine the chapter's tools. When `re.findall` is given a pattern with
**several capture groups**, it returns a list of **tuples** -- one per match, the
captured pieces inside:

```python
import re

re.findall(r"(\w+)=(\w+)", "host=local port=8080")
# [('host', 'local'), ('port', '8080')]
```

A list of `(key, value)` pairs is exactly what **`dict(...)`** turns into a
dictionary. So one pattern plus `dict` parses a whole config string:

```python
dict(re.findall(r"(\w+)=(\w+)", "host=local port=8080"))
# {'host': 'local', 'port': '8080'}
```

`\w+` matches a run of word characters (letters, digits, underscore), so each key
and value is grabbed whole, and the `=` between them is matched literally.

## Your task

Define `parse_config(text)` that parses a space-separated string of `key=value`
pairs into a dict, using **`re.findall`** with two capture groups.

## Done when

- `parse_config("host=local port=8080")` equals
  `{"host": "local", "port": "8080"}`.
- `parse_config("debug=on")` equals `{"debug": "on"}`.
- `parse_config("")` equals `{}`.
- Pairs are captured with one `(\w+)=(\w+)` pattern, not split by hand.
