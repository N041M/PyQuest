A list can contain other lists — a **nested** list — modelling a grid or table.
`grid[r]` selects an inner list (a row); `grid[r][c]` then selects an item from
it (a column), so two indexes reach one cell.

- The first index picks the row, the second the item within that row.
- A `for row in grid:` loop yields each inner list; nest a second loop
  (`for cell in row:`) to reach every item.
- The inner lists are ordinary lists — mutable and independently sized (rows
  need not be the same length).

```python
grid = [[1, 2, 3],
        [4, 5, 6]]
grid[0][2]    # 3   -- row 0, column 2
grid[1][0]    # 4
```
