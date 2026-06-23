**`d.items()`** vydá každý pár `(klíč, hodnota)`, takže cyklus `for` se dvěma
proměnnými projde celý slovník a každý pár průběžně rozbaluje.

- `for k, v in d.items():` naváže `k` na klíč a `v` na jeho hodnotu při každém
  průchodu.
- `d.keys()` a `d.values()` procházejí jen klíče nebo jen hodnoty; procházení
  slovníku přímo (`for k in d`) prochází **klíče**.
- Pořadí iterace je **pořadí vkládání** (pořadí, v jakém byly klíče poprvé
  přidány).

```python
prices = {"pen": 2, "ink": 5}
for item, cost in prices.items():
    print(item, cost)        # pen 2 / ink 5
```
