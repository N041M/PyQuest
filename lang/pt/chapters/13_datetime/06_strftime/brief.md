# 13.6 -- strftime: formata uma data à tua maneira

## Conceito

`.isoformat()` dá sempre `YYYY-MM-DD`. Quando precisas de um formato
diferente, **`strftime`** ("string format time") apresenta uma data usando
**códigos de formato**:

```python
from datetime import date

d = date(2026, 6, 20)
d.strftime("%d/%m/%Y")     # '20/06/2026'
d.strftime("%Y.%m.%d")     # '2026.06.20'
```

- `%d` é o dia, `%m` o mês, `%Y` o ano com quatro dígitos -- todos preenchidos
  com zeros. Tudo o resto na cadeia de formato (o `/`, o `.`, os espaços) é
  copiado literalmente.
- Existem outros códigos (`%H` hora, `%M` minuto, e códigos de nome como
  `%A`), mas os numéricos são os principais.

Assim, um único objeto de data consegue apresentar-se da forma que um
relatório ou utilizador esperar.

## Exemplo

```python
from datetime import date

def dotted(text):
    return date.fromisoformat(text).strftime("%Y.%m.%d")
```

## A tua tarefa

Define `pretty(text)` que recebe uma cadeia `YYYY-MM-DD` e a devolve no
formato **`DD/MM/YYYY`**, usando `strftime("%d/%m/%Y")` sobre a data
analisada.

## Está feito quando

- `pretty("2026-06-20")` devolve `"20/06/2026"`.
- `pretty("1999-01-05")` devolve `"05/01/1999"` (preenchido com zeros).
- A formatação é feita por `strftime`, não reorganizando pedaços separados.
