**`except ValueError as e:`** liga o objeto da exceção apanhada a um nome,
para que o possas inspecionar — mais simplesmente imprimindo-o para mostrar
o que correu mal.

- O objeto da exceção transporta o detalhe; `str(e)` (ou `print(e)`) produz
  a sua mensagem. `type(e).__name__` dá o nome da classe do erro.
- O nome `e` só existe dentro do bloco `except`.
- Um único handler pode apanhar uma família inteira nomeando uma classe
  base: `except Exception as e:` liga qualquer uma das suas subclasses (usa
  com moderação — apanhar de forma demasiado ampla esconde bugs).

```python
try:
    int("xyz")
except ValueError as e:
    print("bad input:", e)    # bad input: invalid literal for int()...
```
