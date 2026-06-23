# 16.4 -- Závěrečná: vypiš účtenku

## Krok 4 -- závěr, sám

Tentokrát žádný návod. Poskládej díly dohromady.

Napiš funkci `receipt(items)`, kde `items` je seznam dvojic `(name, price)`. Vrátí
víceřádkový řetězec: **jeden řádek na položku** ve tvaru `"name: $price"` (dvě
desetinná místa), pak závěrečný řádek **`"TOTAL: $<total>"`**.

Pro `receipt([("Apple", 1.5), ("Bread", 2.0)])`:

```
Apple: $1.50
Bread: $2.00
TOTAL: $3.50
```

## Hotovo, když

- Každá položka je vlastní řádek, naformátovaný `"name: $price"` na dvě desetinná
  místa.
- Poslední řádek je `"TOTAL: $<součet cen>"`, také na dvě desetinná místa.
- Prázdný seznam vrátí jen `"TOTAL: $0.00"`.
