# 1.11 -- Číslo ze vstupu

## Koncept

`input()` vždy vrátí **text**, i když člověk napíše číslice. Pokud s ním zkusíš
počítat, `+` bude místo sčítání spojovat -- vzpomeň si na úlohu 1.7:

```python
n = input()      # user types 21  ->  n is the string "21"
print(n + n)     # "2121", not 42
```

Pro počítání nejprve **převeď** text na číslo pomocí `int(...)`:

```python
n = int(input())   # "21" -> 21, a real number now
print(n * 2)       # 42
```

`int(...)` vezme text, který vypadá jako celé číslo, a udělá z něj `int`, se kterým
můžeš počítat. Tento vzor -- `int(input())` -- je nesmírně častý.

## Častý omyl

`int` jen „neodstraní uvozovky“; vytvoří jiný typ. Po `int(input())` je hodnota
číslo, takže `+`, `*`, `//` a spol. počítají doopravdy.

## Tvůj úkol

Přečti ze vstupu celé číslo a pak vypiš jeho **dvojnásobek**. Příklady:

- vstup `21` -> výstup `42`
- vstup `0`  -> výstup `0`
- vstup `-5` -> výstup `-10`

Tedy: přečti pomocí `input()`, převeď pomocí `int(...)`, vynásob dvěma a vypiš
výsledek.

## Hotovo, když

- Pro vstup `21` je výstup `42`.
- Funguje to i pro `0` a pro záporné číslo jako `-5` (kontrola je zkouší).
