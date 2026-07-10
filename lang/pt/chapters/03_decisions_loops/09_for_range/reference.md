**`range(n)`** produz os inteiros `0, 1, …, n - 1` — `n` números a começar em
zero — e um ciclo **`for`** executa o seu bloco uma vez para cada um, associando a
variável do ciclo ao valor atual.

- `range(n)` para **antes** de `n` (intervalo semiaberto), pelo que `range(5)` é
  `0,1,2,3,4` — cinco passagens.
- `range(start, stop)` começa em `start`; `range(start, stop, step)` conta de
  `step` em `step` (que pode ser negativo para contar para trás).
- O `range` é preguiçoso (*lazy*) — produz números à medida que são pedidos, sem
  construir uma lista — pelo que um intervalo enorme não custa nada até ser
  percorrido.

```python
for i in range(3):
    print(i)              # 0, 1, 2

for i in range(2, 6):
    print(i)              # 2, 3, 4, 5
```
