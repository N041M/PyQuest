**Devolver** um valor e **imprimi-lo** são ações diferentes, e confundi-las
é um erro comum.

- **`return`** devolve um valor ao código que chamou, que o pode guardar, fazer
  aritmética com ele, ou passá-lo adiante. O valor viaja.
- **`print`** escreve texto no ecrã e devolve `None`. O valor é mostrado mas
  não é capturado — `x = print(5)` faz com que `x` seja `None`.
- Uma função que imprime em vez de devolver não pode ser usada como base para outra coisa. Prefere
  fazer `return` do resultado e deixar que quem **chama** decida se imprime.

```python
def double(n):
    return n * 2        # caller can use it
print(double(5) + 1)    # 11  -- works because double returned
```
