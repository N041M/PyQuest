# 13.5 -- Subtrair datas: dias entre elas

## Conceito

Adicionar uma duração a uma data dá uma data. O inverso também funciona:
**subtrai uma data de outra** e obténs um **`timedelta`** -- o intervalo entre
elas:

```python
from datetime import date

gap = date(2026, 7, 1) - date(2026, 6, 20)
gap            # timedelta(days=11)
gap.days       # 11
```

- `date_b - date_a` é um `timedelta`; o seu **`.days`** é o número inteiro de
  dias entre elas.
- Se `date_b` for **anterior** a `date_a`, `.days` é **negativo**.
- É exato ao longo de meses, anos e dias bissextos -- a biblioteca conta, tu
  não precisas.

## Exemplo

```python
from datetime import date

def days_old(born, today):
    return (date.fromisoformat(today) - date.fromisoformat(born)).days
```

## A tua tarefa

Define `days_between(a, b)` que recebe duas cadeias `YYYY-MM-DD` e devolve o
número de dias **de `a` até `b`** (de modo que um `b` posterior dê um número
positivo), usando subtração de datas.

## Está feito quando

- `days_between("2026-06-20", "2026-07-01")` devolve `11`.
- `days_between("2026-07-01", "2026-06-20")` devolve `-11`.
- `days_between("2026-06-20", "2026-06-20")` devolve `0`.
- A contagem vem de subtrair dois objetos `date`, não de aritmética manual.
