# 6.7 -- Stavění na vestavěných funkcích

## Koncept

Funkce zazáří, když zabalí malý *recept* za dobré jméno. Recept na průměr:

> součet, vydělený počtem

Vlastníš každou přísadu: `sum()` (5.2), `len()` (2.6) a `/` (1.9). Pamatuj z 1.9,
že `/` **vždy vrací float** -- `4 / 2` je `2.0`, ne `2`. To je tady správně: průměr
je přirozeně desetinné číslo.

```python
def average(nums):
    return sum(nums) / len(nums)
```

Jedna funkce, jeden řádek, okamžitě znovupoužitelné -- a jméno říká, co ten řádek
znamená.

## Příklad

```python
average([1, 2])        # 1.5
average([10, 20, 30])  # 20.0
```

## Tvůj úkol

Definuj `average(nums)`, která vrátí průměr neprázdného seznamu čísel.

## Hotovo, když

- `average([1, 2])` vrátí `1.5`; `average([10, 20, 30])` vrátí `20.0`.
- Výsledek je **float**, i když je dělení přesné (použij `/`, ne `//`).
- Jednopoložkový seznam vrátí tu položku (jako float).
