# 13.3 -- weekday: que dia da semana

## Conceito

Dada uma data, que dia da semana é? Calcular isto à mão significa conhecer os
anos bissextos e a duração de cada mês. O objeto `date` já o faz -- basta
perguntar-lhe:

```python
from datetime import date

date(2026, 6, 20).weekday()     # 5  (Saturday)
```

- **`.weekday()`** devolve um inteiro: **segunda-feira é 0**, terça-feira 1,
  ... domingo 6.
- (`.isoweekday()` é a mesma ideia mas segunda-feira=1 .. domingo=7.)

Isto é o tipo de coisa que deixas a biblioteca fazer: ela codifica o
calendário real, por isso a resposta é correta para qualquer data, anos
bissextos incluídos.

## Exemplo

```python
from datetime import date

def is_weekend(text):
    return date.fromisoformat(text).weekday() >= 5
```

## A tua tarefa

Define `weekday(text)` que recebe uma cadeia `YYYY-MM-DD` e devolve o seu dia
da semana como um inteiro, **segunda-feira=0 .. domingo=6**, usando o
`.weekday()` do objeto de data.

## Está feito quando

- `weekday("2026-06-20")` devolve `5` (um sábado).
- `weekday("2000-01-01")` devolve `5`.
- A resposta vem de `.weekday()` sobre um `date` analisado.
