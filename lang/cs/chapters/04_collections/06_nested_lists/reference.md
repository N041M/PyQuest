Seznam může obsahovat jiné seznamy — **vnořený** seznam — modelující mřížku nebo
tabulku. `grid[r]` vybere vnitřní seznam (řádek); `grid[r][c]` pak z něj vybere
položku (sloupec), takže dva indexy dosáhnou na jednu buňku.

- První index vybere řádek, druhý položku v tom řádku.
- Cyklus `for row in grid:` vydá každý vnitřní seznam; vnoř druhý cyklus
  (`for cell in row:`), abys dosáhl na každou položku.
- Vnitřní seznamy jsou obyčejné seznamy — měnitelné a nezávisle velké (řádky
  nemusí mít stejnou délku).

```python
grid = [[1, 2, 3],
        [4, 5, 6]]
grid[0][2]    # 3   -- row 0, column 2
grid[1][0]    # 4
```
