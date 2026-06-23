# 10.7 -- zastav se brzy

## Koncept

Generátor skončí ve chvíli, kdy skončí jeho funkce -- a prosté `return` (bez
hodnoty) uvnitř generátoru znamená „zastav teď, žádné další položky“. Takže generátor
se může rozhodnout **skončit brzy**, dřív než dojde vstup.

```python
def before_blank(words):
    for w in words:
        if w == "":
            return          # stop the generator here
        yield w
```

`list(before_blank(["a", "b", "", "c"]))` je `["a", "b"]` -- jakmile se dosáhne
prázdného, `return` generátor ukončí a `"c"` se nikdy nevyprodukuje.

## Příklad

```python
def while_positive(nums):
    for n in nums:
        if n <= 0:
            return
        yield n

list(while_positive([3, 1, -1, 5]))    # [3, 1]
```

## Tvůj úkol

Definuj generátor `until_zero(nums)`, který yielduje každé číslo **dokud nedosáhne
`0`**, pak se zastaví. Samotná `0` ani nic po ní se **neyielduje**. Pokud žádná `0`
není, yielduje celý seznam.

## Hotovo, když

- `list(until_zero([1, 2, 0, 3]))` je `[1, 2]`.
- `list(until_zero([0, 9]))` je `[]`; `list(until_zero([1, 2, 3]))` je
  `[1, 2, 3]`.
- Použiješ `yield` a zastavíš se brzy, když narazíš na `0`.
