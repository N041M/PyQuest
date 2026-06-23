# 4.9 -- Procházení slovníku

## Koncept

Abys navštívil vše ve slovníku, procházej `.items()`, který dá každý **klíč a
hodnotu** dohromady:

```python
ages = {"sam": 20, "ada": 36}
for name, age in ages.items():
    print(name, age)      # sam 20, then ada 36
```

Část `for name, age in ...` rozbaluje každý pár do dvou proměnných. Slovníky si
pamatují pořadí, ve kterém jsi klíče vložil, takže je dostaneš zpět v tomto pořadí.

Jsou tu také `.keys()` (jen klíče) a `.values()` (jen hodnoty), ale `.items()` je
ten obvyklý, když potřebuješ obojí.

## Příklad

```python
d = {"x": 1, "y": 2}
for k, v in d.items():
    print(f"{k}={v}")     # x=1, then y=2
```

## Tvůj úkol

Přečti počet `n`, pak `n` dvojic **slova** a **čísla** do slovníku. Pak vypiš jeden
řádek `key=value` pro každou dvojici, v pořadí, v jakém byly přidány.

Pro vstup `2`, `a`, `1`, `b`, `2`:

```
a=1
b=2
```

## Hotovo, když

- `a=1`, `b=2` se vypíšou v pořadí vkládání.
- Počet `0` nevypíše nic.
