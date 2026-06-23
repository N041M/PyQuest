# 7.1 -- try / except

## Koncept

Doteď jsi spoustu chyb *způsobil*. Čas jednu **ošetřit**.

Když Python narazí na něco nemožného -- jako `int("hello")` -- **vyvolá výjimku**:
normální tok se zastaví a, pokud se s tím nikdo nevypořádá, program spadne s
traceblackem. `try`/`except` je způsob, jak se s tím vypořádat:

```python
try:
    n = int(text)
    print("a number!")
except ValueError:
    print("not a number")
```

Jak to běží:

- Blok `try` běží normálně -- **dokud** nějaký řádek nevyvolá chybu.
- Pokud nic nevyvolá chybu, blok `except` se zcela přeskočí.
- Pokud `int(text)` vyvolá `ValueError` (jeho stížnost na nepřevoditelný text),
  zbytek bloku `try` se opustí a místo něj se spustí blok `except`. **Žádný pád.**

Program se *zotaví*: zvolil, co znamená selhání, místo aby se skácel.

## Příklad

Vstup `7` vypíše `14`. Vstup `seven` vypíše `not a number` -- stejný kód, žádný pád
v ani jednom případě.

## Tvůj úkol

Přečti jeden řádek. Pokud se převede na celé číslo, vypiš to číslo **zdvojnásobené**.
Pokud ne, vypiš přesně `not a number`. (Tohle je zase skriptová úloha: `input()` a
`print()` jsou zpět.)

## Hotovo, když

- `7` vypíše `14`; `-3` vypíše `-6`.
- `seven` a `12abc` vypíšou `not a number` -- a program skončí čistě, bez
  tracebacku.
- Použil jsi `try`/`except` -- checker vyžaduje skutečnou věc.
