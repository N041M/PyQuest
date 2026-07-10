O módulo **`datetime`** disponibiliza tipos para datas de calendário e horas.
O seu tipo **`date`** guarda um dia como um único objeto: `date(year, month, day)`.

- O construtor **valida** os valores em relação ao calendário real —
  `date(2026, 2, 30)` gera `ValueError`, para que uma data impossível não
  passe despercebida.
- Os atributos `.year`, `.month`, `.day` lêem as partes de volta;
  **`.isoformat()`** apresenta a cadeia padrão `YYYY-MM-DD`, sempre preenchida
  com zeros.
- Um `date` conhece o calendário, por isso consegue comparar (`<`, `==`),
  subtrair (13.5) e indicar o seu dia da semana (13.3) — coisas que três
  números inteiros soltos ou uma cadeia construída à mão não conseguem fazer.
  `date.today()` devolve o dia atual.

```python
from datetime import date

d = date(2026, 6, 20)
d.month          # 6
d.isoformat()    # '2026-06-20'
date(2026, 1, 5).isoformat()   # '2026-01-05'  -- padded
```
