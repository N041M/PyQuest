Dividir por zero levanta **`ZeroDivisionError`**. Apanhá-lo demonstra o
estilo **EAFP** — "mais fácil pedir perdão do que permissão": tentas a
operação e tratas da falha, em vez de testares antecipadamente todos os
casos maus.

- `a / 0` e `a // 0` e `a % 0` levantam todos esta exceção. Envolver a
  divisão num `try` permite-te fornecer uma alternativa quando o divisor
  acaba por ser zero.
- O EAFP muitas vezes lê-se de forma mais limpa do que um `if b != 0:` de
  guarda, e evita uma corrida entre a verificação e a utilização.

```python
try:
    rate = hits / total
except ZeroDivisionError:
    rate = 0.0           # no data yet -- sensible fallback
```
