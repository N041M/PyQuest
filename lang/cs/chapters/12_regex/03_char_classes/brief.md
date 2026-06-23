# 12.3 -- Znakové třídy: [aeiou]

## Koncept

**Znaková třída** `[...]` odpovídá **kterémukoli jednomu** ze znaků uvedených uvnitř:

```python
import re

re.findall(r"[aeiou]", "education")     # ['e', 'u', 'a', 'i', 'o']
```

- `[aeiou]` odpovídá jedné samohlásce; `[abc]` odpovídá `a`, `b` nebo `c`.
- **Rozsah** používá pomlčku: `[a-z]` je libovolné malé písmeno, `[0-9]` libovolná
  číslice (totéž co `\d`), `[A-Za-z0-9]` libovolné písmeno nebo číslice.
- Úvodní `^` třídu **neguje**: `[^aeiou]` je libovolný znak, který *není* samohláska.

Třída je jeden znak; přidej kvantifikátor (`[a-z]+`), abys odpovídal jejich úseku.

## Příklad

```python
import re

def count_letters(text):
    return len(re.findall(r"[a-z]", text))
```

## Tvůj úkol

Pomocí znakové třídy s **`re.findall`** definuj `count_vowels(text)`, která vrátí,
kolik samohlásek (`a e i o u`) je v `text`.

## Hotovo, když

- `count_vowels("education")` vrátí `5`, `count_vowels("xyz")` vrátí `0`.
- `count_vowels("")` vrátí `0`.
- Počítání používá `re.findall` se třídou `[aeiou]`, ne ruční kontrolu `in`.
