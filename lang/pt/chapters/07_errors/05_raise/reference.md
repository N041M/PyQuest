**`raise`** dispara uma exceção **por ti próprio**, parando a função e
sinalizando que algo está errado. Permite que o teu código rejeite entradas
inválidas no momento em que são detetadas, tal como fazem as funções nativas.

- `raise ValueError("amount must be positive")` constrói uma exceção com uma
  mensagem e lança-a; a execução para a menos que um `try` mais acima na
  cadeia de chamadas a apanhe.
- Escolhe o tipo que se adequa: `ValueError` para um valor errado, `TypeError`
  para um tipo errado. A mensagem explica o que era esperado.
- Levantar a exceção na fronteira (assim que a entrada chega) mantém o resto
  do código capaz de confiar nos seus dados.

```python
def withdraw(amount):
    if amount <= 0:
        raise ValueError("amount must be positive")
    ...
```
