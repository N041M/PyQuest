Um **`timedelta`** representa uma **duração** — um intervalo de tempo, não um
ponto nele. Adicionar um a um `date` produz outro `date`, com toda a
contabilidade do calendário (duração dos meses, fronteiras de ano, dias
bissextos) tratada automaticamente.

- `timedelta(days=n)` é `n` dias; também aceita `weeks=`, `hours=`,
  `minutes=`, `seconds=`. `n` pode ser **negativo** para se mover para trás.
- `date + timedelta` e `date - timedelta` dão uma nova data; subtrair duas
  *datas* dá um `timedelta` (13.5).
- É por isso que a aritmética de datas passa pela biblioteca: `date(2026, 12, 25) +
  timedelta(days=10)` avança corretamente para o ano seguinte, e a duração de
  fevereiro nunca é problema teu.

```python
from datetime import date, timedelta

date(2026, 6, 20) + timedelta(days=40)    # date(2026, 7, 30)
date(2026, 1, 1) - timedelta(days=1)      # date(2025, 12, 31)
date(2026, 6, 20) + timedelta(weeks=2)    # date(2026, 7, 4)
```
