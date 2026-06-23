Příkaz **`if`** spustí odsazený blok **jen když** je jeho podmínka pravdivá.
Podmínka se vyhodnotí na boolean; je-li pravdivá, blok se spustí; je-li
nepravdivá, přeskočí se a program pokračuje níže.

- Blok je vymezen **odsazením** (obvykle 4 mezery). Každý řádek odsazený pod `if`
  k němu patří; první řádek zpět na vnější úrovni ho ukončí.
- Podmínka nemusí být doslovné `True`/`False` — testuje se **pravdivost** libovolné
  hodnoty: `0`, `0.0`, `""` a prázdné kolekce jsou nepravdivé; vše ostatní je
  pravdivé.

```python
if temperature > 30:
    print("hot")        # runs only when the test is True
print("done")           # always runs -- not indented under the if
```
