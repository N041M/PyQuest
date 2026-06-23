**`enumerate(items)`** spáruje každou položku s její pozicí, takže cyklus `for`
dostane obojí najednou — žádné ručně držené počítadlo.

- `for i, item in enumerate(lst):` naváže `i` na index (od 0) a `item` na hodnotu
  při každém průchodu.
- Druhý argument nastaví **počáteční číslo**: `enumerate(lst, 1)` čísluje od 1, což
  se hodí pro seznamy určené lidem.
- Je líný (vydává dvojice na vyžádání) a funguje na libovolném iterovatelném
  objektu.

```python
for i, name in enumerate(["a", "b"], 1):
    print(i, name)        # 1 a / 2 b
```
