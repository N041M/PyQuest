Objekt drží **stav** — data, která přetrvávají mezi voláními. Metoda může
**zmutovat** `self` a další volání metody tu změnu vidí, takže si objekt pamatuje,
co se s ním stalo.

- `self.count += 1` aktualizuje atribut na místě; nová hodnota žije, dokud se zase
  nezmění.
- To je smysl objektů: nesou svá data s sebou napříč voláními, na rozdíl od prosté
  funkce, jejíž lokální proměnné zmizí, když vrátí hodnotu.
- Každá instance má **vlastní** kopii atributů, takže dva čítače počítají nezávisle.

```python
class Counter:
    def __init__(self):
        self.n = 0
    def tick(self):
        self.n += 1         # remembered for next time

c = Counter(); c.tick(); c.tick(); c.n   # 2
```
