Um único `try` pode ser seguido por **vários `except`**, cada um a tratar
de uma falha diferente com a sua própria resposta. São testados de cima
para baixo; o **primeiro** tipo correspondente corre, e os restantes são
ignorados.

- Isto constrói um tratamento robusto de entradas: um `try` à volta do
  trabalho, depois um `except` por cada coisa que pode correr mal
  (`ValueError` para um número inválido, `ZeroDivisionError` para `/0`),
  cada um dando uma mensagem à medida.
- Ordena do específico para o geral se os tipos estiverem relacionados, já
  que o primeiro a corresponder ganha.

```python
try:
    a, b = int(x), int(y)
    print(a / b)
except ValueError:
    print("please enter whole numbers")
except ZeroDivisionError:
    print("cannot divide by zero")
```
