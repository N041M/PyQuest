# 4.12 -- Kombinování množin

## Koncept

Množiny lze kombinovat jako v matematice:

- **průnik** `a & b` -- položky v **obou**
- **sjednocení** `a | b` -- položky v **kterékoli**
- **rozdíl** `a - b` -- položky v `a`, ale ne v `b`

```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)    # {2, 3}
print(a | b)    # {1, 2, 3, 4}
print(a - b)    # {1}
```

Tyto odpovídají na otázky jako „které položky dvě skupiny sdílejí?“ bez psaní
cyklu. (`a.intersection(b)` a `a.union(b)` dělají totéž co `&` a `|`.)

## Příklad

```python
x = {"a", "b"}
y = {"b", "c"}
print(len(x & y))   # 1   (just "b")
```

## Tvůj úkol

Přečti první skupinu: počet `n`, pak `n` slov. Pak druhou skupinu: počet `m`, pak
`m` slov. Vypiš, **kolik odlišných slov se objeví v obou** skupinách.

Pro první skupinu `a`, `b` a druhou skupinu `b`, `c`:

```
1
```

(V obou je jen `b`.)

## Hotovo, když

- `{a, b}` a `{b, c}` vypíšou `1`.
- Prázdné skupiny dají `0`; duplicity uvnitř skupiny se počítají jednou.
