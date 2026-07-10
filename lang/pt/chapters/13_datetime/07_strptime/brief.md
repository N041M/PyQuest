# 13.7 -- strptime: analisar segundo um formato

## Conceito

`date.fromisoformat` só lê o único formato ISO. Para **qualquer** formato --
uma data com uma hora, uma ordem personalizada -- usa **`datetime.strptime`**
("parse time"). Dás-lhe a cadeia **e** um formato que a descreve, com os
mesmos códigos do `strftime`:

```python
from datetime import datetime

dt = datetime.strptime("2026-06-20 14:30", "%Y-%m-%d %H:%M")
dt.year     # 2026
dt.hour     # 14
dt.minute   # 30
```

- O formato tem de corresponder à forma da cadeia; uma incompatibilidade gera
  `ValueError`, por isso valida enquanto analisa.
- O resultado é um **`datetime`** -- uma data *e* uma hora -- com os
  atributos `.year`, `.month`, `.day`, `.hour`, `.minute`, `.second`.

`strptime` analisa, `strftime` formata: os mesmos códigos, sentidos opostos.

## Exemplo

```python
from datetime import datetime

def year_of(text):
    return datetime.strptime(text, "%Y-%m-%d %H:%M").year
```

## A tua tarefa

Define `hour_of(text)` que recebe uma marca temporal como
`"2026-06-20 14:30"` e devolve a **hora** como um inteiro, analisando-a com
`datetime.strptime` e o formato `"%Y-%m-%d %H:%M"`.

## Está feito quando

- `hour_of("2026-06-20 14:30")` devolve `14`.
- `hour_of("1999-01-05 09:05")` devolve `9`.
- A hora vem de um `datetime` analisado, não de recorte de cadeia.
