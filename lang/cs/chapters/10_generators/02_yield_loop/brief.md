# 10.2 -- yield uvnitř cyklu

## Koncept

Skutečná síla `yield` se ukáže, když sedí **uvnitř cyklu**: jeden řádek `yield`
proběhne jednou na průchod a proudí celou transformovanou posloupnost -- hodnotu po
hodnotě, nikdy ne celý seznam najednou.

```python
def letters(word):
    for ch in word:
        yield ch.upper()
```

`list(letters("hi"))` je `["H", "I"]`. Cyklus prochází vstup; `yield` pokaždé vydá
jednu transformovanou položku a mezitím se pozastaví.

## Příklad

```python
def doubles(nums):
    for x in nums:
        yield x * 2
```

`list(doubles([1, 5, 9]))` je `[2, 10, 18]`.

## Tvůj úkol

Definuj generátor `squares(n)`, který **yielduje** druhé mocniny celých čísel od `0`
až po (ale ne včetně) `n`: `0, 1, 4, 9, ...`. Je-li `n` `0` (nebo méně), nevyzve
nic.

## Hotovo, když

- `list(squares(4))` je `[0, 1, 4, 9]`.
- `list(squares(1))` je `[0]`; `list(squares(0))` je `[]`.
- Použiješ `yield` uvnitř cyklu -- ne vrácený seznam nebo komprehenzi.
