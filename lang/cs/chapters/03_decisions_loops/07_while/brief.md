# 3.7 -- while

## Koncept

**Cyklus `while`** opakuje blok, **dokud** podmínka zůstává `True`. Zkontroluje
podmínku, spustí blok, pak zkontroluje znovu -- stále dokola:

```python
count = 1
while count <= 3:
    print(count)
    count = count + 1   # move toward making the condition False
# prints 1, 2, 3
```

Řádek `count = count + 1` je zásadní: mění `count`, takže se podmínka nakonec stane
`False`. Bez něj se cyklus nikdy nezastaví.

## Častý omyl -- nekonečný cyklus

Pokud se podmínka nikdy nestane `False`, cyklus běží navždy. Vždy se ujisti, že se
něco uvnitř cyklu posouvá k bodu zastavení. (Pokud se zdá, že program zamrzl, je to
obvykle nekonečný cyklus.)

## Příklad

```python
n = 4
i = 1
while i <= n:
    print(i)
    i = i + 1
# prints 1, 2, 3, 4
```

## Tvůj úkol

Přečti celé číslo `n` a pak vypiš každé číslo od `1` do `n`, každé na vlastním
řádku, pomocí cyklu `while`.

Pro vstup `3` je výstup:

```
1
2
3
```

## Hotovo, když

- `3` vypíše `1`, `2`, `3`. `1` vypíše jen `1`.
- `0` (nebo záporné) nevypíše nic -- tělo cyklu se nikdy nespustí.
