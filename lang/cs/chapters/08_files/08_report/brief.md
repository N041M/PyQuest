# 8.8 -- Závěrečná: žebříčková zpráva

## Koncept

Tato závěrečná úloha je skutečný malý program: přečti soubor záznamů, seřaď je podle
pořadí a zapiš naformátovanou zprávu -- s použitím split (4.4), rozbalování (4.7),
`int()` (1.11), `sorted` s klíčem (5.4), f-řetězců (2.10) a souborů (tato kapitola)
dohromady.

`scores.txt` má jeden záznam na řádek, jméno a skóre oddělené mezerou:

```
alice 40
bob 25
cara 40
```

Každý řádek se rozdělí na svá dvě pole:

```python
name, score = line.split()
score = int(score)
```

Chceš, aby `ranking.txt` vypsal hráče od nejvyššího skóre po nejnižší (shody v
abecedním pořadí), pak závěrečný řádek se součtem:

```
alice - 40
cara - 40
bob - 25
Total: 105
```

Všimni si přesného formátu: `jméno - skóre` na hráče (mezery kolem pomlčky) a
závěrečný řádek `Total: <součet>`.

## Tvůj úkol

Přečti `scores.txt` a zapiš `ranking.txt` s jedním řádkem `jméno - skóre` na hráče
seřazeným podle skóre (nejvyšší první, shody abecedně), následovaným závěrečným
řádkem `Total: <součet všech skóre>`.

## Hotovo, když

- Hráči jsou vypsáni `jméno - skóre`, nejvyšší skóre první, shody abecedně.
- Poslední řádek je `Total: ` následované součtem každého skóre.
- Jednohráčový soubor funguje a pro oba soubory jsi použil `with`.
