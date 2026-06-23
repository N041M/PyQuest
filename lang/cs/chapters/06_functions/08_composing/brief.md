# 6.8 -- Funkce volající funkce

## Koncept

Tvé funkce mohou volat **jedna druhou**. To je opravdový tahák: vyřeš malý problém
jednou, pojmenuj ho a postav na něm další funkci.

```python
def clean(text):
    return text.strip().lower()

def same_word(a, b):
    return clean(a) == clean(b)
```

`same_word` neopakuje recept ořež-a-zmenši -- *deleguje* na `clean`. Pokud `clean`
někdy vylepšíš (řekněme, že bude odstraňovat i interpunkci), každá funkce na něm
postavená se vylepší zadarmo. Opakování receptu na obou místech je způsob, jak se
rodí chyby: opravíš jednu kopii, na druhou zapomeneš.

Všimni si, že `same_word` vrací výsledek porovnání -- **boolean** (`True`/`False`),
jako v 3.1. Žádné `if` není potřeba: `clean(a) == clean(b)` už *je* odpovědí.

## Příklad

```python
clean("  Tea ")              # "tea"
same_word("  Tea ", "tea")   # True
same_word("tea", "milk")     # False
```

## Tvůj úkol

Definuj **obě** funkce:

- `clean(text)` -- vrátí text s oříznutými okolními mezerami a malými písmeny (2.7).
- `same_word(a, b)` -- vrátí `True` právě tehdy, když jsou oba texty po vyčištění
  stejné. Musí **volat `clean`**, ne recept opakovat.

## Hotovo, když

- `clean("  Tea ")` vrátí `"tea"`.
- `same_word("  Tea ", "tea")` je `True`; `same_word("tea", "milk")` je `False`.
- `same_word` volá `clean` -- checker hledá tu delegaci.
