Os **operadores booleanos** combinam condições:

- **`and`** é verdadeiro apenas quando **ambos** os lados são verdadeiros.
- **`or`** é verdadeiro quando **pelo menos um** dos lados é verdadeiro.
- **`not`** inverte um único valor.

Fazem **avaliação em curto-circuito** (*short-circuit*): o `and` para no primeiro operando
falso, o `or` no primeiro verdadeiro, pelo que o lado direito não é avaliado quando o
esquerdo já decide o resultado. A precedência é `not` > `and` > `or`; os parênteses
tornam a intenção óbvia.

```python
0 < x and x < 100      # True only inside the range
done or out_of_time    # True if either holds
not finished           # flips the flag
```
