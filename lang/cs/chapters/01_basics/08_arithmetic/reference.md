Aritmetické operátory jsou `+` (sčítání), `-` (odčítání), `*` (násobení), `/`
(dělení), `//` (celočíselné dělení), `%` (zbytek) a `**` (mocnina).

Řídí se **prioritou** (pořadím operací), od nejvyšší po nejnižší:

1. `**`
2. unární `-` (negace)
3. `*`, `/`, `//`, `%`
4. `+`, `-`

Operátory se stejnou prioritou se vyhodnocují **zleva doprava**, kromě `**`, který
je pravě asociativní (`2 ** 3 ** 2` je `2 ** 9`). **Závorky** tohle všechno
přebijí — vyhodnotí se jako první.

```python
2 + 3 * 4      # 14   -- * before +
(2 + 3) * 4    # 20   -- parentheses first
-3 ** 2        # -9   -- ** before unary minus
```
