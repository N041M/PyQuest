# 13.2 -- fromisoformat: de texto para data

## Conceito

As datas costumam chegar como **texto** -- de um ficheiro, um formulário, uma
API. **`date.from
isoformat`** analisa uma cadeia padrão `YYYY-MM-DD` e produz
um objeto `date` real, o inverso de `.isoformat()`:

```python
from datetime import date

d = date.fromisoformat("2026-06-20")
d.year      # 2026
d.month     # 6
d.day       # 20
```

- Devolve um `date`, por isso podes depois ler `.year` / `.month` / `.day`,
  comparar a data ou fazer aritmética com ela -- tudo o que uma data consegue
  fazer.
- Espera exatamente a forma `YYYY-MM-DD`; uma cadeia malformada gera
  `ValueError`.

Analisar para uma data real (em vez de recortares a cadeia tu próprio)
significa que o valor fica validado e pronto para trabalho de calendário.

## Exemplo

```python
from datetime import date

def month_of(text):
    return date.fromisoformat(text).month
```

## A tua tarefa

Usando **`date.fromisoformat`**, define `parts(text)` que analisa uma cadeia
`YYYY-MM-DD` e devolve o tuplo de inteiros `(year, month, day)` lidos a partir
dos atributos do objeto de data.

## Está feito quando

- `parts("2026-06-20")` devolve `(2026, 6, 20)`.
- `parts("1999-01-05")` devolve `(1999, 1, 5)`.
- Os valores vêm dos atributos de um `date` analisado, não de
  `text.split("-")`.
