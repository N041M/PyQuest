# 12.4 -- Kvantifikátory: + znamená jednou nebo víckrát

## Koncept

**Kvantifikátor** říká, kolikrát se vzor před ním smí opakovat:

- **`+`** -- jednou nebo víckrát (`[a-z]+` je úsek jednoho či více malých písmen)
- **`*`** -- nulakrát nebo víckrát
- **`?`** -- volitelné (nula nebo jedna)
- **`{n}`** -- přesně `n`; **`{n,m}`** -- mezi `n` a `m`

```python
import re

re.findall(r"[A-Za-z]+", "Hello, world!")     # ['Hello', 'world']
```

Bez `+` by `[A-Za-z]` odpovídalo jednotlivým písmenům po jednom. `+` ho přiměje
pochytat **celé slovo** a zastavit se u prvního znaku, který nesedí (mezera, čárka,
číslice). Takto rozdělíš text na slova a přitom ignoruješ interpunkci.

## Příklad

```python
import re

def integers(text):
    return re.findall(r"\d+", text)
```

## Tvůj úkol

Pomocí **`re.findall`** s kvantifikátorem definuj `find_words(text)`, která vrátí
seznam slov v `text` -- každé úsek jednoho či více písmen (`[A-Za-z]+`), s ignorovanou
interpunkcí a mezerami.

## Hotovo, když

- `find_words("Hello, world!")` vrátí `["Hello", "world"]`.
- `find_words("one-two three")` vrátí `["one", "two", "three"]`.
- `find_words("")` vrátí `[]`.
- Slova jsou nalezena pomocí `[A-Za-z]+`, ne rozdělena ručně.
