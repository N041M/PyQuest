A **lista** é uma sequência ordenada e mutável de valores, escrita entre parênteses retos:
`[10, 20, 30]`. A lista vazia é `[]`. Os itens são acedidos por índice tal como os
caracteres de uma cadeia de caracteres (`lst[0]`, `lst[-1]`).

- **`.append(x)`** adiciona `x` ao **fim**, aumentando a lista em um. Altera a
  lista no próprio local e devolve `None` (por isso nunca escrevas `lst = lst.append(x)`).
- O padrão de construir a partir do vazio: começa com `[]`, depois usa `.append` uma
  vez por cada passagem de um ciclo para juntar resultados.
- Ao contrário das cadeias de caracteres, uma lista pode conter valores de tipos diferentes.

```python
nums = []
for i in range(3):
    nums.append(i * i)   # -> [0, 1, 4]
```
