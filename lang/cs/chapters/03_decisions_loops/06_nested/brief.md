# 3.6 -- Vnořené podmínky

## Koncept

Blok `if` může obsahovat **další** `if`. Tomu se říká **vnořování**. Vnitřní
kontrola proběhne jen tehdy, když je vnější podmínka už pravdivá. Každá úroveň je
odsazená o krok dál.

```python
if logged_in:
    if is_admin:
        print("admin panel")
    else:
        print("user page")
else:
    print("please log in")
```

Zde se `is_admin` kontroluje jen tehdy, když je `logged_in` pravdivé.

## Příklad

```python
n = 250
if n > 0:
    if n < 100:
        print("small")
    else:
        print("big")
else:
    print("non-positive")
# prints: big
```

## Tvůj úkol

Přečti celé číslo a zařaď ho:

- je-li **0 nebo záporné**, vypiš `non-positive`;
- jinak (je kladné) vypiš `small`, je-li **menší než 100**, nebo `big`, je-li
  **100 a více**.

Použij vnořený `if` (vnější kontrola na kladnost, vnitřní na velikost).

Pro vstup `42` je výstup:

```
small
```

## Hotovo, když

- `-1` a `0` vypíšou `non-positive`; `42` vypíše `small`; `100` a `500` vypíšou
  `big`.
