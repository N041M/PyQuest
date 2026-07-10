O Python tem três operadores de divisão:

- **`/` divisão verdadeira** produz sempre um **`float`**, mesmo quando o resultado é
  inteiro: `7 / 2 == 3.5`, e `4 / 2 == 2.0` (repara no `.0`).
- **`//` divisão inteira** divide e arredonda *para baixo*, em direção ao infinito negativo,
  dando um `int` para dois inteiros: `7 // 2 == 3`. Com um operando negativo continua a
  arredondar para baixo, por isso `-7 // 2 == -4`, não `-3`.
- **`%` resto (módulo)** é o que sobra: `7 % 2 == 1`. Em Python o
  resultado tem o **sinal do divisor**, por isso `-7 % 2 == 1`.

Para quaisquer inteiros, `a == (a // b) * b + (a % b)` é verdade. `divmod(a, b)` devolve o
par `(a // b, a % b)` de uma só vez. Dividir por zero levanta `ZeroDivisionError`.

```python
17 / 5    # 3.4
17 // 5   # 3
17 % 5    # 2   -- 3*5 + 2 == 17
```
