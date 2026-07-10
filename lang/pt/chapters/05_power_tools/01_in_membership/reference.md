O operador **`in`** testa a pertença e devolve um booleano, por isso encaixa diretamente
num `if` ou `while`. `x in c` é `True` quando `x` é encontrado em `c`.

- Para uma **cadeia de caracteres**, `in` testa uma **substring**: `"cat" in "concatenate"` é
  `True`.
- Para uma **lista** ou **tuplo**, testa um item (percorrendo a sequência).
- Para um **dicionário** ou **conjunto**, testa uma **chave**/membro — e é rápido
  (baseado em hash), ao contrário da procura linear de uma lista.
- `x not in c` é a negação, e lê-se de forma natural.

```python
"a" in "cat"          # True
3 in [1, 2, 3]        # True
"key" in {"key": 1}   # True  -- tests keys
```
