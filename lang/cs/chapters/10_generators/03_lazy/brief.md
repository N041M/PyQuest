# 10.3 -- generátory jsou líné

## Koncept

Tohle je superschopnost. Generátor odvede práci jen tehdy, **když požádáš o další
hodnotu**. Nikdy nestaví celou posloupnost předem -- takže generátor může být
**nekonečný** a přesto téměř nic nestát, dokud z něj netaháš.

```python
def naturals():
    i = 0
    while True:        # never stops on its own...
        yield i
        i = i + 1
```

`while True` v normální funkci by zamrzlo navždy. V generátoru je v pořádku: každý
`yield` cyklus **pozastaví**, dokud volající nechce ještě jeden. Vezmeš si jen tolik,
kolik potřebuješ:

```python
from itertools import islice
list(islice(naturals(), 4))     # [0, 1, 2, 3] -- then it just stops asking
```

`islice(gen, k)` vytáhne z generátoru prvních `k` položek a víc ne. Generátor
vyprodukuje přesně tyto čtyři, pak sedí pozastavený.

## Příklad

`naturals()` výše yielduje `0, 1, 2, 3, ...` bez konce. Vytažení 3 položek dá
`[0, 1, 2]`; vytažení 10 dá `[0, 1, ..., 9]`. Tentýž nekonečný generátor, požádaný o
různá množství.

## Tvůj úkol

Definuj **nekonečný** generátor `naturals()`, který yielduje celá čísla začínající
od `0`: `0, 1, 2, 3, ...` navždy. Nikdy se nesmí zastavit sám od sebe; checker z něj
vždy vytáhne jen hrstku hodnot.

## Hotovo, když

- Prvních 5 hodnot `naturals()` je `[0, 1, 2, 3, 4]`.
- Je nekonečný -- vytažení dalších hodnot prostě dá další čísla; nikdy nedojde.
- Použiješ `yield`, takže volání `naturals()` vrátí generátor.
