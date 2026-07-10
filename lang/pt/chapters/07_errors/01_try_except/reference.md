Uma instrução **`try` / `except`** corre código arriscado e apanha o erro se
falhar, em vez de deixar o programa cair. O bloco `try` contém o código que
pode **levantar** uma exceção; o bloco `except` só corre se isso acontecer.

- Se o bloco `try` for bem-sucedido, o `except` é completamente ignorado.
- Se uma instrução em `try` levantar uma exceção, o **resto do `try` é
  abandonado** e o controlo salta para o `except` correspondente; o programa
  continua depois disso.
- Um erro não apanhado desenrola o programa inteiro com um traceback —
  `except` é a forma de intervires.

```python
try:
    n = int(text)        # may raise ValueError
except ValueError:
    n = 0                # recover instead of crashing
```
