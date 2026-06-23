# 3.8 -- Cyklus do zarážky (sentinel)

## Koncept

Cyklus nemusí počítat. Může běžet, dokud uživatel nezadá speciální hodnotu
**zarážku** (sentinel), která znamená „stop“. Trik je přečíst jednou *před* cyklem
a pak číst znovu *na konci* každého průchodu:

```python
line = input()
while line != "quit":
    print("you said:", line)
    line = input()        # read the next one
print("done")
```

Cyklus běží, dokud vstup není zarážka (zde `"quit"`). Jakmile zarážka přijde,
podmínka je nepravdivá a cyklus skončí.

## Příklad

Čti čísla a sčítej je, dokud není zadána `0`:

```python
total = 0
n = int(input())
while n != 0:
    total = total + n
    n = int(input())
print(total)
```

## Tvůj úkol

Čti celá čísla, jedno na řádek, a sčítej je. Zastav se, když je zadána `0` (`0`
nepřičítej). Pak vypiš součet.

Pro vstup `4`, `5`, `0` je výstup:

```
9
```

## Hotovo, když

- `4`, `5`, `0` vypíše `9`; samotná `0` vypíše `0`.
- Samotná `0` se nepřičítá; čísla mohou být záporná.
