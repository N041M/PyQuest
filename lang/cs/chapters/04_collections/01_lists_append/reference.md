**Seznam** je uspořádaná, měnitelná posloupnost hodnot, psaná v hranatých
závorkách: `[10, 20, 30]`. Prázdný seznam je `[]`. K položkám se dostaneš indexem
stejně jako ke znakům řetězce (`lst[0]`, `lst[-1]`).

- **`.append(x)`** přidá `x` na **konec** a zvětší seznam o jednu položku. Mění
  seznam na místě a vrací `None` (takže nikdy nepiš `lst = lst.append(x)`).
- Vzor stavění z prázdna: začni `[]`, pak `.append` jednou za každý průchod cyklu,
  abys posbíral výsledky.
- Na rozdíl od řetězců může seznam držet hodnoty různých typů.

```python
nums = []
for i in range(3):
    nums.append(i * i)   # -> [0, 1, 4]
```
