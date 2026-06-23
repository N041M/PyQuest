# 6.9 -- Rekurze: funkce volající sebe sama

## Koncept

Funkce může volat **sebe sama**. Tomu se říká **rekurze** a funguje vždy, když
problém obsahuje menší kopii téhož problému.

Faktoriál je klasika: `5!` znamená `5 * 4 * 3 * 2 * 1`. Ale podívej se znovu:

> `5!` je prostě `5 * 4!` -- a `4!` je `4 * 3!` ...

Rekurzivní funkce přesně tohle vyjadřuje, plus **základní případ** -- nejmenší
vstup zodpovězený přímo, bez dalších volání:

```python
def fact(n):
    if n == 0:
        return 1            # base case: 0! is 1
    return n * fact(n - 1)  # the smaller copy of the same problem
```

`fact(3)` proběhne jako `3 * fact(2)` -> `3 * 2 * fact(1)` -> `3 * 2 * 1 * fact(0)`
-> `3 * 2 * 1 * 1` = `6`. Bez základního případu by se volání nikdy nezastavila --
rekurzivní verze nekonečného cyklu.

Faktoriál bys mohl spočítat cyklem `for` -- ale *lekce* je tady to volání sebe sama,
takže tato úloha ho vyžaduje.

## Příklad

```python
fact(0)    # 1
fact(3)    # 6
fact(5)    # 120
```

## Tvůj úkol

Definuj `fact(n)`, která vrátí `n!` **rekurzivně**: základní případ pro `0` a
`n * fact(n - 1)` pro zbytek. `n` nikdy není záporné.

## Hotovo, když

- `fact(0)` je `1`, `fact(1)` je `1`, `fact(5)` je `120`.
- `fact` volá sebe sama -- checker hledá volání sebe sama, takže verze s cyklem
  neprojde.
