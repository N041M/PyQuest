# 1.3 -- Volba oddělovače

## Koncept

Když dáš `print` více hodnot, ve výchozím stavu je spojí mezerou. Tento spojovací
řetězec můžeš změnit speciálním nastavením zvaným **`sep`** (zkratka za
*separator*, oddělovač).

Takové nastavení se píše jako `jméno=hodnota` uvnitř závorek, za tvými hodnotami:

```python
print("a", "b", "c", sep="-")
```

zobrazí:

```
a-b-c
```

`sep="-"` říká `print`, aby mezi hodnoty vkládal pomlčku místo mezery. Oddělovač
jde pouze *mezi* hodnoty -- ne před první ani za poslední. Jako oddělovač můžeš
použít libovolný text: `sep=", "`, `sep=""` (nic), `sep="/"` a tak dále.

`sep` se musí napsat přesně, bez mezery před `=`, a hodnota v uvozovkách, protože
je to text.

## Příklad

```python
print("home", "user", "docs", sep="/")
```

zobrazí:

```
home/user/docs
```

## Tvůj úkol

Vypiš přesně toto datum pomocí tří **čísel** spojených pomlčkami:

```
2024-12-25
```

Předej `2024`, `12`, `25` jedinému `print` a nastav `sep` tak, aby byly spojeny
`-`. Nepiš pomlčky sám jako součást textu.

## Hotovo, když

- Výstup je přesně `2024-12-25`.
- Vznikne ze tří čísel plus nastavení `sep`, ne z jednoho napsaného řetězce.
