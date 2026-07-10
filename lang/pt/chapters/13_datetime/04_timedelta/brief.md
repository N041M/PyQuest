# 13.4 -- timedelta: aritmética de datas

## Conceito

Um **`timedelta`** é uma **duração** -- um intervalo de tempo. Adiciona um a
uma data e obténs outra data, com toda a confusão do calendário (duração dos
meses, mudança de ano, dias bissextos) tratada por ti:

```python
from datetime import date, timedelta

date(2026, 6, 20) + timedelta(days=40)     # date(2026, 7, 30)
date(2026, 12, 25) + timedelta(days=10)    # date(2027, 1, 4)  -- crosses the year
```

- `timedelta(days=n)` é uma duração de `n` dias (também aceita `weeks=`,
  `hours=`, etc.). `n` pode ser **negativo** para ir para trás.
- `date + timedelta` dá um novo `date`; `date - timedelta` vai no sentido
  contrário.
- É por isso que nunca fazes contas de datas à mão: a biblioteca sabe que
  fevereiro tem 29 dias num ano bissexto, e tu não precisas de saber.

## Exemplo

```python
from datetime import date, timedelta

def tomorrow(text):
    return (date.fromisoformat(text) + timedelta(days=1)).isoformat()
```

## A tua tarefa

Define `add_days(text, n)` que recebe uma cadeia `YYYY-MM-DD` e um inteiro
`n`, e devolve a cadeia `YYYY-MM-DD` da data `n` dias depois (usando
`timedelta`). `n` pode ser negativo.

## Está feito quando

- `add_days("2026-06-20", 40)` devolve `"2026-07-30"`.
- `add_days("2026-01-01", -1)` devolve `"2025-12-31"`.
- O deslocamento usa `timedelta` sobre um `date` real, não uma contagem de
  dias feita à mão.
