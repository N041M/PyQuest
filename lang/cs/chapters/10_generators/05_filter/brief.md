# 10.5 -- filtruj během yieldování

## Koncept

Generátor nemusí yieldovat při každém průchodu. Dej `yield` za `if` a stream
**filtruješ**, jak teče -- přeskakuješ položky, které nechceš, a vydáváš jen ty,
které ano.

```python
def shouts(words):
    for w in words:
        if w.isupper():
            yield w          # only the all-caps words come out
```

`list(shouts(["hi", "STOP", "go", "NOW"]))` je `["STOP", "NOW"]`. Cyklus navštíví
každé slovo; `yield` proběhne jen tehdy, když je `if` pravdivý.

## Příklad

```python
def positives(nums):
    for n in nums:
        if n > 0:
            yield n
```

`list(positives([-1, 4, 0, 2]))` je `[4, 2]`.

## Tvůj úkol

Definuj generátor `evens(nums)`, který yielduje jen **sudá** čísla z `nums` a
zachová jejich původní pořadí. (Číslo je sudé, když `n % 2 == 0`.) Pokud žádné není
sudé, nevyzve nic.

## Hotovo, když

- `list(evens([1, 2, 3, 4]))` je `[2, 4]`.
- `list(evens([1, 3, 5]))` je `[]`; `list(evens([]))` je `[]`.
- Použiješ `yield` za `if` -- ne vrácený seznam nebo komprehenzi.
