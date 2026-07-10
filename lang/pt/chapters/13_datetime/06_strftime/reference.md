**`strftime(format)`** ("string-format-time") apresenta uma data ou datetime
numa cadeia que descreves com **códigos de formato**. Onde `.isoformat()` dá
um formato fixo, `strftime` dá qualquer formato.

- Códigos comuns: `%Y` ano com quatro dígitos, `%m` mês, `%d` dia — todos
  preenchidos com zeros; `%H` hora, `%M` minuto, `%S` segundo. Quaisquer
  outros caracteres (`/`, `.`, espaços) são copiados literalmente.
- Códigos de nome como `%A` (dia da semana) e `%B` (mês) **dependem da
  configuração regional**, por isso prefere os códigos numéricos para
  resultados que têm de ser estáveis.
- `strptime` é o inverso — ele *analisa* uma cadeia segundo um formato (13.7).

```python
from datetime import date

d = date(2026, 6, 20)
d.strftime("%d/%m/%Y")     # '20/06/2026'
d.strftime("%Y%m%d")       # '20260620'
d.strftime("%d.%m.%y")     # '20.06.26'  -- %y is the 2-digit year
```
