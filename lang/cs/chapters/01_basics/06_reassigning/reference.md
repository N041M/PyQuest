Proměnná je jméno, ne krabice: opětovné přiřazení jméno **znovu sváže** s novou
hodnotou. Jméno vždy drží své nejnovější přiřazení; předchozí hodnota přes něj
prostě už není dosažitelná.

- Každé `=` nahradí to, na co jméno ukazuje. Na pořadí záleží — pozdější přiřazení
  vítězí.
- Pravá strana se vyhodnotí pomocí *aktuální* hodnoty jména, pak se výsledek znovu
  sváže, takže `x = x + 1` přečte staré `x` a uloží nové.
- Složené tvary (`x += 1`, `x *= 2`, …) jsou zkratkou přesně pro tohle: přečíst,
  zkombinovat, znovu svázat.

```python
score = 10
score = 25        # score is now 25
score = score + 5 # reads 25, stores 30
```
