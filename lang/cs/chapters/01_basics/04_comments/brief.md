# 1.4 -- Komentáře

## Koncept

**Komentář** je poznámka v kódu, kterou Python ignoruje. Cokoli za `#` na řádku se
při běhu programu přeskočí. Komentáře jsou pro lidi -- vysvětlují, co kód dělá.

```python
# This whole line is a note and does nothing.
print("Hi")   # Text after # on a code line is also ignored.
```

Výše se spustí pouze `print("Hi")`. Obě poznámky se přeskočí.

Druhé, velmi praktické využití: **zakomentování** kódu. Když dáš `#` před řádek
skutečného kódu, ten řádek přestane běžet -- aniž bys ho smazal. Takto řádek
dočasně vypneš.

```python
# print("off")
print("on")
```

Vypíše se pouze `on`; první řádek je teď komentář.

## Častý omyl

Dát `#` před řádek ho **nesmaže** ani nezpůsobí chybu -- řádek se prostě nespustí.
Odeber `#` a spustí se znovu.

## Tvůj úkol

Výchozí soubor už obsahuje řádek, který vypíše `Hidden`. **Zakomentuj ho**, aby se
nespustil -- **nemaž** ho -- a přidej řádek, který vypíše `Visible`.

Program musí vypsat pouze:

```
Visible
```

## Hotovo, když

- Výstup je přesně `Visible`.
- Řádek `print("Hidden")` je stále v souboru, ale zakomentovaný pomocí `#`, takže
  se nespustí. (Tato úloha je o *zakomentování*, takže smazání řádku se nepočítá.)
