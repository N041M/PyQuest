# 7.7 -- Čtení chyby: except ... as e

## Koncept

Výjimka není jen signál -- je to **objekt nesoucí zprávu**. Zachyť ji *do
proměnné* pomocí `as` a můžeš tu zprávu použít:

```python
try:
    n = int(text)
except ValueError as e:
    print(e)
```

Pro `text = "5x"` to vypíše Pythonovu vlastní diagnózu:

```
invalid literal for int() with base 10: '5x'
```

`e` je objekt chyby; jeho vypsání ukáže jeho zprávu. Takto skutečné programy logují,
co se opravdu pokazilo, místo vágního „něco selhalo“ -- rozdíl mezi hlášením bugu,
podle kterého můžeš jednat, a tím, podle kterého ne.

(Zprávu tu nepíšeš sám -- *předáváš* tu, kterou Python připojil, když chybu
vyvolal.)

## Příklad

Vstup `7` vypíše `7`. Vstup `5x` vypíše
`invalid literal for int() with base 10: '5x'`.

## Tvůj úkol

Přečti jeden řádek. Pokud se převede na celé číslo, vypiš to číslo. Pokud ne, chyť
`ValueError` **jako `e`** a vypiš samotné `e` -- Pythonovu zprávu, ne svou vlastní.

## Hotovo, když

- `7` vypíše `7`.
- `5x` vypíše přesnou zprávu `invalid literal ...: '5x'` -- s urážlivým textem v ní
  v uvozovkách.
- Zprávu jsi nenapsal ručně (musí sedět pro *jakýkoli* vstup, což trefí jen
  vypsání `e`).
