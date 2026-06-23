**`elif`** („else if“) přidá další větve mezi `if` a `else`. Python kontroluje
každou podmínku **popořadě** a spustí blok **první**, která je pravdivá, pak
zbytek přeskočí. Volitelné závěrečné `else` ošetří „nic nesedělo“.

- Spustí se vždy jen jedna větev — první pravdivá. Pozdější podmínky se ani
  nevyhodnotí.
- Protože vítězí první shoda, na pořadí záleží: konkrétnější nebo přednostní testy
  dej dopředu.
- Řetěz `elif` je plošší a jasnější než vnořování `if` do každého `else`.

```python
if score >= 90:
    grade = "A"
elif score >= 80:       # only checked if the first was False
    grade = "B"
else:
    grade = "C"
```
