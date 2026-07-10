Uma string é **iterável**, pelo que um ciclo `for` percorre-a **um carácter de cada vez**,
por ordem, associando a variável do ciclo a cada carácter. Não indexas manualmente.

- Cada passagem dá uma string de um único carácter; o ciclo executa-se `len(s)` vezes.
- Esta é a forma direta de examinar ou contabilizar caracteres — combina-a com um `if`
  dentro do ciclo para agir sobre determinados caracteres.
- A mesma forma `for ... in` percorre qualquer sequência (listas, ranges, …), não
  apenas strings.

```python
for ch in "cat":
    print(ch)             # c, then a, then t
```
