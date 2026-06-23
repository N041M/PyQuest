# 4.10 -- Chybějící klíče a .get()

## Koncept

Vyhledání klíče, který ve slovníku není, pomocí `d[key]` **spadne** (`KeyError`):

```python
ages = {"sam": 20}
print(ages["lee"])    # KeyError!
```

`.get()` je bezpečný způsob. Pro chybějící klíč vrátí `None` místo pádu -- nebo
**výchozí hodnotu**, kterou dodáš:

```python
print(ages.get("lee"))        # None
print(ages.get("lee", 0))     # 0      (your default)
print(ages.get("sam", 0))     # 20     (key exists, so its value)
```

Takže `d.get(key, default)` znamená „hodnota, pokud klíč existuje, jinak
`default`“.

## Příklad

```python
d = {"a": 1}
print(d.get("a", 0))    # 1
print(d.get("z", 0))    # 0
```

## Tvůj úkol

Přečti počet `n`, pak `n` dvojic slova a čísla do slovníku. Pak přečti **dotazové
slovo** a vypiš jeho číslo -- ale pokud slovo ve slovníku není, vypiš místo toho
`0` (nespadni).

Pro vstup `2`, `a`, `1`, `b`, `2`, pak dotaz `c`:

```
0
```

(`c` není klíč, takže se vypíše výchozí `0`.)

## Hotovo, když

- Přítomný klíč vypíše svou hodnotu; chybějící klíč vypíše `0`.
- Při chybějícím klíči nikdy nespadne (použij `.get`).
