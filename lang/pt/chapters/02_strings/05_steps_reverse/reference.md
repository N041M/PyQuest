Uma fatia leva uma terceira parte, o **passo**: `s[start:stop:step]` retira cada
caractere de `step` em `step`. O passo por omissão é 1.

- `s[::2]` retira cada segundo caractere (índices 0, 2, 4, …).
- Um passo **negativo** anda para trás. `s[::-1]` é a forma idiomática de
  **inverter** uma cadeia; com um passo negativo, o início/fim por omissão invertem-se para
  o fim e o início.
- `s[::-2]` retira cada segundo caractere, do fim para o início.

```python
s = "Python"
s[::2]    # 'Pto'
s[::-1]   # 'nohtyP'  -- reversed
```
