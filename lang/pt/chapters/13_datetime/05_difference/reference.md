Subtrair um `date` de outro produz um **`timedelta`** — o intervalo entre
eles — e o seu atributo **`.days`** é o número inteiro de dias, calculado com
exatidão ao longo de meses, anos e dias bissextos.

- `date_b - date_a` mede de `a` até `b`: se `b` for **anterior**, `.days` é
  **negativo**, por isso o sinal indica-te a direção.
- O resultado é uma duração, por isso compõe-se: adiciona-a de volta a uma
  data, multiplica-a, compara dois intervalos.
- Este é o contraponto de contagem de adicionar um `timedelta` (13.4) —
  juntos, tornam as datas numa pequena álgebra: `date + duration = date`,
  `date - date = duration`.

```python
from datetime import date

(date(2026, 7, 1) - date(2026, 6, 20)).days     # 11
(date(2026, 6, 20) - date(2026, 7, 1)).days     # -11
(date(2026, 3, 1) - date(2024, 3, 1)).days      # 730  -- 2024 was a leap year
```
