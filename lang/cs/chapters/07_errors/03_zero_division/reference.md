Dělení nulou vyvolá **`ZeroDivisionError`**. Jeho zachycení předvádí styl **EAFP**
— „snazší žádat o odpuštění než o povolení“: zkus operaci a ošetři selhání, místo
abys nejprve testoval každý špatný případ.

- `a / 0` i `a // 0` i `a % 0` vyvolají chybu. Obalení dělení do `try` ti umožní
  dodat náhradní hodnotu, když se dělitel ukáže být nula.
- EAFP se často čte čistěji než hlídací `if b != 0:` a vyhne se závodu mezi
  kontrolou a použitím.

```python
try:
    rate = hits / total
except ZeroDivisionError:
    rate = 0.0           # no data yet -- sensible fallback
```
