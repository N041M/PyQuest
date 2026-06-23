**`range(n)`** vytvoří celá čísla `0, 1, …, n - 1` — `n` čísel začínajících od
nuly — a cyklus **`for`** spustí svůj blok jednou pro každé, přičemž řídicí
proměnnou naváže na aktuální hodnotu.

- `range(n)` se zastaví **před** `n` (polootevřený), takže `range(5)` je
  `0,1,2,3,4` — pět průchodů.
- `range(start, stop)` začne na `start`; `range(start, stop, step)` počítá po
  `step` (který může být záporný pro odpočet).
- `range` je líný — vydává čísla na vyžádání, aniž by stavěl seznam — takže
  obrovský rozsah nic nestojí, dokud se neprochází.

```python
for i in range(3):
    print(i)              # 0, 1, 2

for i in range(2, 6):
    print(i)              # 2, 3, 4, 5
```
