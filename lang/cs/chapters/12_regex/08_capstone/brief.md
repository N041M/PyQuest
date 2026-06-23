# 12.8 -- Závěrečná: parsování konfigurace key=value

## Koncept

Čas zkombinovat nástroje kapitoly. Když `re.findall` dostane vzor s **několika
zachytávacími skupinami**, vrátí seznam **n-tic** -- jednu na shodu, se zachycenými
kousky uvnitř:

```python
import re

re.findall(r"(\w+)=(\w+)", "host=local port=8080")
# [('host', 'local'), ('port', '8080')]
```

Seznam dvojic `(klíč, hodnota)` je přesně to, co **`dict(...)`** promění ve slovník.
Takže jeden vzor plus `dict` rozparsuje celý konfigurační řetězec:

```python
dict(re.findall(r"(\w+)=(\w+)", "host=local port=8080"))
# {'host': 'local', 'port': '8080'}
```

`\w+` odpovídá úseku znaků slova (písmena, číslice, podtržítko), takže každý klíč a
hodnota se pochytá celý a `=` mezi nimi se shoduje doslovně.

## Tvůj úkol

Definuj `parse_config(text)`, která rozparsuje mezerami oddělený řetězec dvojic
`key=value` na slovník, pomocí **`re.findall`** se dvěma zachytávacími skupinami.

## Hotovo, když

- `parse_config("host=local port=8080")` se rovná
  `{"host": "local", "port": "8080"}`.
- `parse_config("debug=on")` se rovná `{"debug": "on"}`.
- `parse_config("")` se rovná `{}`.
- Dvojice jsou zachyceny jedním vzorem `(\w+)=(\w+)`, ne rozděleny ručně.
