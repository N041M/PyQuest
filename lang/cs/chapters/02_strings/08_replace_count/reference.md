Dvě metody pro hledání a přehled:

- **`s.replace(old, new)`** vrátí nový řetězec s **každým** nepřekrývajícím se
  výskytem `old` nahrazeným `new`. Nahradí všechny shody, ne jen první; pokud se
  `old` nevyskytne, řetězec se vrátí beze změny.
- **`s.count(sub)`** vrátí, kolikrát se `sub` vyskytuje, počítá nepřekrývající se
  shody zleva doprava. `"aaa".count("aa")` je `1`, ne 2.

Obě jen čtou `s` a vracejí novou informaci; původní řetězec zůstává nedotčen.

```python
"a-b-c".replace("-", "_")   # 'a_b_c'  -- every match
"banana".count("a")          # 3
```
