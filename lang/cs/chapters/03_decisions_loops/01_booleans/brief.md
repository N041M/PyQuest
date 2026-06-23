# 3.1 -- Booleany a porovnávání

## Koncept

**Boolean** je hodnota, která je buď `True`, nebo `False` -- odpověď ano/ne. Je to
vlastní typ (`bool`), psaný s velkým písmenem.

Booleany získáš **porovnáváním** hodnot:

| operátor | význam |
|---|---|
| `==` | rovná se |
| `!=` | nerovná se |
| `<`  | menší než |
| `>`  | větší než |
| `<=` | menší nebo rovno |
| `>=` | větší nebo rovno |

```python
print(3 < 5)      # True
print(3 == 5)     # False
print(7 >= 7)     # True
```

Pozor, `==` (porovnání) jsou **dvě** rovnítka. Jedno `=` proměnnou *přiřadí*; `==`
se *ptá „rovnají se?“*.

## Příklad

```python
a = 4
b = 9
print(a > b)      # False
```

## Tvůj úkol

Přečti dvě celá čísla (každé na vlastním řádku). Vypiš, zda je **první větší než
druhé** -- tedy vypiš výsledek `first > second` (bude to `True`, nebo `False`).

Pro vstup `8` a pak `3` je výstup:

```
True
```

## Hotovo, když

- Pro `8` a pak `3` vypíše `True`; pro `2` a pak `5` vypíše `False`.
- Když se obě čísla rovnají, vypíše `False` (rovno není „větší“).
