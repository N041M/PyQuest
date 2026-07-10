# 12.8 -- Capstone: analisar configuração key=value

## Conceito

Está na hora de combinar as ferramentas do capítulo. Quando `re.findall` recebe
um padrão com **vários grupos de captura**, devolve uma lista de **tuplos** --
um por correspondência, com as partes capturadas dentro:

```python
import re

re.findall(r"(\w+)=(\w+)", "host=local port=8080")
# [('host', 'local'), ('port', '8080')]
```

Uma lista de pares `(key, value)` é exatamente o que **`dict(...)`**
transforma num dicionário. Assim, um padrão mais `dict` analisa uma cadeia de
configuração inteira:

```python
dict(re.findall(r"(\w+)=(\w+)", "host=local port=8080"))
# {'host': 'local', 'port': '8080'}
```

`\w+` corresponde a uma sequência de caracteres de palavra (letras, dígitos,
sublinhado), por isso cada chave e valor é capturado por inteiro, e o `=`
entre eles é correspondido literalmente.

## A tua tarefa

Define `parse_config(text)` que analisa uma cadeia de pares `key=value`
separados por espaços num dicionário, usando **`re.findall`** com dois grupos
de captura.

## Está feito quando

- `parse_config("host=local port=8080")` é igual a
  `{"host": "local", "port": "8080"}`.
- `parse_config("debug=on")` é igual a `{"debug": "on"}`.
- `parse_config("")` é igual a `{}`.
- Os pares são capturados com um único padrão `(\w+)=(\w+)`, não divididos à
  mão.
