# 12.5 -- Grupos: captura as partes

## Conceito

Parênteses **`(...)`** num padrão marcam um **grupo de captura**: uma parte da
correspondência que queres extrair. O objeto de correspondência devolve depois
cada um deles:

```python
import re

m = re.match(r"(\d+)-(\d+)-(\d+)", "2026-06-20")
m.group(1)     # '2026'
m.group(2)     # '06'
m.groups()     # ('2026', '06', '20')
```

- `re.match` corresponde a partir do **início** da cadeia de caracteres e
  devolve um objeto de correspondência (ou `None`).
- `m.group(n)` devolve o texto que o *n*-ésimo grupo capturou (`group(0)` é a
  correspondência inteira); `m.groups()` devolve todos eles como um tuplo.
- O texto capturado continua a ser uma cadeia de caracteres -- `int(m.group(1))`
  se quiseres um número.

Assim, um único padrão verifica o formato e extrai os campos.

## Exemplo

```python
import re

def split_pair(text):
    m = re.match(r"(\w+):(\w+)", text)
    return (m.group(1), m.group(2))
```

## A tua tarefa

Usando **`re.match`** com grupos de captura, define `parse_date(text)` que
recebe uma data como `"2026-06-20"` e devolve o tuplo de **inteiros**
`(year, month, day)`.

## Está feito quando

- `parse_date("2026-06-20")` devolve `(2026, 6, 20)`.
- `parse_date("1999-01-05")` devolve `(1999, 1, 5)`.
- Os campos vêm de grupos de captura, não de `text.split("-")`.
