Uma lista pode conter outras listas — uma lista **aninhada** — modelando uma
grelha ou tabela. `grid[r]` seleciona uma lista interna (uma linha); `grid[r][c]`
depois seleciona um item dentro dela (uma coluna), pelo que dois índices chegam a
uma célula.

- O primeiro índice escolhe a linha, o segundo o item dentro dessa linha.
- Um ciclo `for row in grid:` produz cada lista interna; aninha um segundo ciclo
  (`for cell in row:`) para chegar a cada item.
- As listas internas são listas normais — mutáveis e de tamanho independente (as
  linhas não têm de ter o mesmo comprimento).

```python
grid = [[1, 2, 3],
        [4, 5, 6]]
grid[0][2]    # 3   -- row 0, column 2
grid[1][0]    # 4
```
