# 13.1 -- date: um dia do calendário

## Conceito

O módulo **`datetime`** modela datas de calendário e horas reais. O seu tipo
**`date`** guarda um único dia -- ano, mês, dia -- como um único objeto:

```python
from datetime import date

d = date(2026, 6, 20)
d.year      # 2026
d.isoformat()   # '2026-06-20'
```

- `date(year, month, day)` constrói o objeto e **valida-o**: `date(2026,
  13, 1)` gera um erro, porque não existe o mês 13.
- `.isoformat()` apresenta-o como a cadeia padrão `YYYY-MM-DD`, preenchida com zeros.
- Um `date` é muito melhor do que três números inteiros soltos: conhece o
  calendário, por isso consegue comparar-se, subtrair-se e formatar-se.

## Exemplo

```python
from datetime import date

def new_year(year):
    return date(year, 1, 1).isoformat()
```

## A tua tarefa

Usando **`date`** de `datetime`, define `iso(y, m, d)` que constrói a data e
devolve a sua cadeia `YYYY-MM-DD` através de `.isoformat()`.

## Está feito quando

- `iso(2026, 6, 20)` devolve `"2026-06-20"`.
- `iso(1999, 1, 5)` devolve `"1999-01-05"` (repara no preenchimento com zeros).
- A cadeia vem do `.isoformat()` de um objeto `date`, não de formatação manual.
