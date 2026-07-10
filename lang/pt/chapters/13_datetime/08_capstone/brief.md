# 13.8 -- Capstone: deslocar uma marca temporal

## Conceito

Isto junta o capítulo todo numa única viagem de ida e volta: **analisar** uma
marca temporal, **deslocá-la** por uma duração, **formatar** o resultado de
volta -- cada passo uma ferramenta que já conheces.

```python
from datetime import datetime, timedelta

dt = datetime.strptime("2026-06-20 23:30", "%Y-%m-%d %H:%M")  # parse
dt = dt + timedelta(hours=2)                                  # shift
dt.strftime("%Y-%m-%d %H:%M")                                 # '2026-06-21 01:30'
```

Repara que o deslocamento passou da meia-noite para o dia seguinte -- a
biblioteca trata disso automaticamente, ao longo de dias, meses e anos.
Fazer isto à mão significaria reimplementar o calendário e o relógio.

## A tua tarefa

Define `add_hours(timestamp, hours)` que recebe uma cadeia
`"YYYY-MM-DD HH:MM"` e um número inteiro de `hours` (que pode ser negativo),
e devolve a marca temporal deslocada por essas horas, no **mesmo formato
`"YYYY-MM-DD HH:MM"`**.

Usa `datetime.strptime` para analisar, `timedelta(hours=...)` para deslocar,
e `strftime` para formatar.

## Está feito quando

- `add_hours("2026-06-20 23:30", 2)` devolve `"2026-06-21 01:30"`.
- `add_hours("2026-01-01 00:30", -1)` devolve `"2025-12-31 23:30"`.
- O deslocamento usa `timedelta` sobre um `datetime` analisado, formatado com
  `strftime` -- não aritmética manual sobre a cadeia.
