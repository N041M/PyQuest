**`date.fromisoformat(text)`** analisa uma cadeia padrão `YYYY-MM-DD` e
produz um objeto `date` — o inverso de `.isoformat()`. O resultado é uma data
real, por isso podes ler os seus atributos, comparar ou fazer aritmética com
ela.

- Espera exatamente a forma ISO; uma cadeia malformada ou impossível gera
  `ValueError`, o que valida a entrada como efeito secundário.
- `.year`, `.month`, `.day` lêem os componentes de volta como inteiros.
- Analisar para uma data (em vez de recortares o texto tu próprio) é o
  objetivo: o valor fica verificado e imediatamente pronto para trabalho de
  calendário. Para formatos que não sejam ISO, `datetime.strptime` analisa
  segundo um formato explícito (13.7).

```python
from datetime import date

d = date.fromisoformat("2026-06-20")
(d.year, d.month, d.day)     # (2026, 6, 20)
d < date.fromisoformat("2026-12-31")   # True
```
