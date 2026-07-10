**`enumerate(items)`** empareira cada item com a sua posição, para que um ciclo `for` obtenha
ambos de uma vez — sem contador guardado à mão.

- `for i, item in enumerate(lst):` liga `i` ao índice (a partir de 0) e `item` ao
  valor, em cada passagem.
- Um segundo argumento define o **número inicial**: `enumerate(lst, 1)` numera
  a partir de 1, útil para listas voltadas para pessoas.
- É preguiçoso (produz pares por pedido) e funciona em qualquer iterável.

```python
for i, name in enumerate(["a", "b"], 1):
    print(i, name)        # 1 a / 2 b
```
