Colocar um **`yield` dentro de um ciclo** transmite uma sequência inteira em
fluxo: o gerador emite um valor transformado por passagem, pausando após
cada um e retomando no pedido seguinte.

- `for x in source: yield f(x)` produz `f(x)` para cada item — a forma
  geradora de construir uma lista com uma compreensão, mas produzida de
  forma preguiçosa.
- Nada é calculado até que algo itere o gerador, e só até onde for consumido.

```python
def squares(nums):
    for n in nums:
        yield n * n

list(squares([1, 2, 3]))    # [1, 4, 9]
```
