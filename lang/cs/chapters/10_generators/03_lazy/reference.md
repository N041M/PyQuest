Generátory jsou **líné**: každá hodnota se spočítá až na vyžádání, takže generátor
může popisovat **nekonečnou** posloupnost a přesto být užitečný — prostě si vezmeš
hodnoty, které potřebuješ.

- Nekonečné `while True: yield n; n += 1` samo o sobě nikdy neskončí, ale
  konzument může zastavit dříve (`break`, nebo několik volání `next`).
- Línost znamená, že generátor pro posloupnost drží v podstatě **žádnou paměť** —
  drží jen svůj aktuální stav, ne každou hodnotu — na rozdíl od seznamu, který je
  všechny zhmotní.

```python
def naturals():
    n = 0
    while True:
        yield n             # endless, but only as far as asked
        n += 1

g = naturals(); next(g), next(g)   # (0, 1)
```
