# 10.1 -- yield: funkce, která se pozastaví

## Koncept

Normální funkce `return`ne **jednou** a je hotová. **Generátor** je funkce, která
místo toho používá `yield`: každý `yield` vrátí **jednu** hodnotu a funkci přesně
tam **pozastaví**. Požádej o další hodnotu a funkce se **obnoví** tam, kde se
zastavila.

```python
def two_words():
    yield "hello"
    yield "world"
```

Jeho zavolání tělo **nespustí**. Podá ti **generátor** -- objekt, ze kterého taháš
hodnoty po jedné, obvykle cyklem `for`:

```python
for w in two_words():
    print(w)        # hello, then world
```

Odměna: generátor vytváří posloupnost **bez stavění celého seznamu v paměti**.
Pocítíš to v 10.3.

## Příklad

```python
def count_up(n):
    i = 1
    while i <= n:
        yield i
        i = i + 1
```

`list(count_up(3))` je `[1, 2, 3]` -- každý průchod cyklu vyzve jedno číslo, pak se
pozastaví, dokud není požádán o další.

## Tvůj úkol

Definuj generátor `count_down(n)`, který **yielduje** celá čísla od `n` dolů k `1`,
v tomto pořadí. Je-li `n` `0` (nebo méně), nevyzve nic.

## Hotovo, když

- `list(count_down(5))` je `[5, 4, 3, 2, 1]`.
- `list(count_down(1))` je `[1]`; `list(count_down(0))` je `[]`.
- Použiješ `yield` -- takže volání `count_down` vrátí generátor, ne seznam.
