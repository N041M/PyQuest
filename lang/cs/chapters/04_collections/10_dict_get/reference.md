**`d.get(key, default)`** vyhledá klíč bezpečně: vrátí hodnotu, je-li klíč
přítomen, jinak `default` — bez vyvolání chyby. Bez výchozí hodnoty vrátí pro
chybějící klíč `None`.

- Použij ho místo `d[key]`, kdykoli je chybějící klíč normální, očekávaný případ,
  ne chyba.
- Pohání **sčítací** idiom: `counts[k] = counts.get(k, 0) + 1` přečte průběžný
  počet (poprvé 0) a zapíše nový.
- `.get` jen čte; nikdy klíč nevloží (na rozdíl od `setdefault`).

```python
ages = {"Ada": 36}
ages.get("Ada", 0)     # 36
ages.get("Nobody", 0)  # 0  -- no KeyError
```
