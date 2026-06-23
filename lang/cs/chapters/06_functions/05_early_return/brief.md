# 6.5 -- return ukončí funkci

## Koncept

`return` nejen předá hodnotu -- také **funkci na místě zastaví**. Nic za provedeným
`return` se neprovede. Díky tomu se větvící funkce čtou přehledně: vyřeš každý
případ a odejdi.

```python
def sign(n):
    if n < 0:
        return "negative"
    if n == 0:
        return "zero"
    return "positive"
```

Všimni si, že tu není žádné `else` -- není potřeba. Pokud vystřelil první `return`,
funkce už skončila; dosáhnout posledního řádku *znamená*, že `n` bylo kladné. Tomuto
stylu se říká **časný return** (early return).

Funkce s několika příkazy `return` stále vrací přesně **jednu** hodnotu na volání:
ten `return`, který se provede první.

## Příklad

```python
sign(-3)    # "negative"
sign(0)     # "zero"
sign(42)    # "positive"
```

## Tvůj úkol

Definuj `sign(n)`, která pro celé číslo `n` vrátí `"negative"`, `"zero"`, nebo
`"positive"`.

## Hotovo, když

- `sign(-3)`, `sign(0)`, `sign(42)` vrátí tři výše uvedená slova.
- Hraniční případy `-1` a `1` jsou také správně.
