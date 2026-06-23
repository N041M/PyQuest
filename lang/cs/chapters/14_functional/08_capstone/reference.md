Závěrečná úloha zřetězí funkce vyššího řádu kapitoly do **datového potrubí** —
podoby velké části skutečného zpracování:

1. **`filter(lambda r: r[1] >= threshold, records)`** zúží na záznamy, které
   kvalifikují;
2. **`sorted(..., key=lambda r: r[1], reverse=True)`** je seřadí podle skóre, od
   nejvyššího po nejnižší (stabilně, takže stejná skóre si ponechají pořadí);
3. **`map(lambda r: r[0], ...)`** vyprojektuje jen pole, které chceš — jméno.

Každá fáze bere funkci a iterovatelný objekt a vydá další iterovatelný objekt,
takže se přímo skládají: filtr napájí řazení, řazení napájí mapování. Stejné potrubí
by se dalo napsat komprehenzemi; vyjádřit ho jako `filter`/`sorted`/`map` je
funkcionální styl a vidět úlohu *jako* potrubí transformací je dovednost, ke které
kapitola směřuje.

```python
def passing(records, threshold):
    qualified = filter(lambda r: r[1] >= threshold, records)
    ranked = sorted(qualified, key=lambda r: r[1], reverse=True)
    return list(map(lambda r: r[0], ranked))
```
