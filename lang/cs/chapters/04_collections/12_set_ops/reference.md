Množiny podporují algebru kolekcí:

- **`a & b`** (průnik) — položky v **obou**.
- **`a | b`** (sjednocení) — položky v **kterékoli**.
- **`a - b`** (rozdíl) — položky v `a`, ale **ne** v `b`.

Každá vrátí **novou** množinu. (`^` je symetrický rozdíl — v právě jedné.) Tyto
vyjadřují množinové otázky přímo a nahrazují ručně psané cykly, které porovnávají
dvě kolekce.

```python
a, b = {1, 2, 3}, {2, 3, 4}
a & b     # {2, 3}
a | b     # {1, 2, 3, 4}
a - b     # {1}
```
