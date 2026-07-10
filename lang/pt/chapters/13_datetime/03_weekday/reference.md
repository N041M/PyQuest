**`date.weekday()`** devolve o dia da semana como um inteiro,
**segunda-feira = 0** até **domingo = 6**. Como um `date` codifica o
calendário real — anos bissextos, meses de duração variável — calcula isto
corretamente para qualquer data, que é exatamente o tipo de trabalho que
delegas na biblioteca em vez de deduzires à mão.

- `.isoweekday()` é o mesmo mas **segunda-feira = 1 .. domingo = 7** (a
  convenção ISO).
- Um uso comum é `weekday() >= 5` para testar se é fim de semana.
- O companheiro `.strftime("%A")` formata o **nome** do dia da semana, mas
  isso depende da configuração regional; o `.weekday()` numérico é estável em
  qualquer lugar.

```python
from datetime import date

date(2026, 6, 20).weekday()      # 5  (Saturday)
date(2026, 6, 22).weekday()      # 0  (Monday)
date(2026, 6, 20).weekday() >= 5 # True -- it's the weekend
```
