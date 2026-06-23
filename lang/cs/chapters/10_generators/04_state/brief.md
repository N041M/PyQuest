# 10.4 -- generátor si pamatuje

## Koncept

Protože se generátor **pozastaví** místo dokončení, jeho lokální proměnné zůstávají
naživu mezi `yield`y. Hodnota, kterou buduješ, přežije každou pauzu -- generátor
naváže přesně tam, kde přestal, i s akumulátorem.

```python
def tally(words):
    seen = 0
    for w in words:
        seen = seen + 1
        yield seen          # 1, then 2, then 3, ... -- `seen` is remembered
```

`list(tally(["a", "b", "c"]))` je `[1, 2, 3]`. Počítadlo `seen` se při každém
průchodu neresetuje; drží si svou hodnotu napříč yieldy.

## Příklad

```python
def running_max(nums):
    best = None
    for n in nums:
        if best is None or n > best:
            best = n
        yield best
```

`list(running_max([3, 1, 5]))` je `[3, 3, 5]` -- každá položka je největší viděná
**dosud**.

## Tvůj úkol

Definuj generátor `running_total(nums)`, který yielduje **průběžný součet** `nums`:
každá hodnota je součet všech čísel až po aktuální včetně. Prázdný seznam nevyzve
nic.

## Hotovo, když

- `list(running_total([3, 1, 2]))` je `[3, 4, 6]`.
- `list(running_total([5]))` je `[5]`; `list(running_total([]))` je `[]`.
- Použiješ `yield` a proměnnou, která nese součet napříč yieldy.
