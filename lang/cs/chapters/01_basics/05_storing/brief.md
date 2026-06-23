# 1.5 -- Uložení hodnoty

## Koncept

**Proměnná** je jméno, které drží hodnotu, abys ji mohl použít později. Vytvoříš
ji pomocí `=`, znaku **přiřazení**:

```python
score = 100
```

Čti to jako „ať je `score` rovno `100`.“ Jméno jde nalevo, hodnota napravo. Po
tomto řádku znamená napsání `score` kdekoli hodnotu `100`.

To se liší od `==` (s nímž se setkáš později u porovnávání). Jediné `=` *ukládá*.

Jakmile je hodnota uložená, můžeš jméno použít, kolikrát chceš:

```python
score = 100
print(score)
print(score)
```

zobrazí:

```
100
100
```

Všimni si, že `print(score)` nemá kolem `score` **žádné uvozovky**. Uvozovky by z
toho udělaly doslovný text „score“; bez uvozovek to znamená hodnotu proměnné,
`100`.

## Pravidla pojmenování (stručně)

Jméno proměnné může obsahovat písmena, číslice a podtržítka, ale nesmí začínat
číslicí a nesmí obsahovat mezery. Používej srozumitelná jména: `total`,
`user_name`, `count`.

## Tvůj úkol

Ulož číslo `42` do proměnné a pak tuto proměnnou vypiš **dvakrát**, aby výstup
byl:

```
42
42
```

V obou případech použij proměnnou -- nepiš `42` přímo do printů.

## Hotovo, když

- Výstup je `42` na dvou samostatných řádcích.
- Oba řádky vznikají vypsáním tvé proměnné (bez uvozovek kolem jejího jména).
