# 10.8 -- Závěrečná: proudové potrubí

## Koncept

Nic nového -- tato závěrečná úloha je kapitola v miniatuře. Skutečný důvod, proč na
generátorech záleží, je, že se **skládají**: výstup jednoho generátoru je vstupem
druhého, takže data tečou skrz **potrubí** (pipeline), po jedné položce, aniž by se
mezitím kdy stavěl celý seznam.

Fáze potrubí je prostě generátor, který prochází `stream` (libovolný iterovatelný
objekt -- seznam, nebo *jiný generátor*) a průběžně yielduje:

```python
def only_long(stream):
    for word in stream:
        if len(word) >= 4:
            yield word
```

Postavíš zdroj, filtr a přeznačkovací fázi, pak je propojíš dohromady.

## Příklad

```python
numbers(4)                              # yields 0, 1, 2, 3
keep_even(numbers(4))                   # yields 0, 2
labelled(keep_even(numbers(4)))         # yields "#0", "#2"
```

## Tvůj úkol

Definuj **tři** generátory:

- `numbers(n)` -- yielduje `0, 1, ..., n-1` (zdroj). `n <= 0` nevyzve nic.
- `keep_even(stream)` -- yielduje jen sudá čísla ze `stream` (libovolný iterovatelný
  objekt).
- `labelled(stream)` -- yielduje řetězec `"#x"` pro každé `x` ve `stream` (např. `7`
  se stane `"#7"`).

Každý musí použít `yield`. `keep_even` a `labelled` musí fungovat na **libovolném**
streamu, včetně výstupu jiného generátoru, aby se skládaly.

## Hotovo, když

- `list(numbers(4))` je `[0, 1, 2, 3]`; `list(numbers(0))` je `[]`.
- `list(keep_even([1, 2, 3, 4]))` je `[2, 4]`.
- `list(labelled([0, 2]))` je `["#0", "#2"]`.
- `list(labelled(keep_even(numbers(6))))` je `["#0", "#2", "#4"]`.
- Všechny tři používají `yield` a filtrovací/přeznačkovací fáze přijímají libovolný
  iterovatelný objekt.
