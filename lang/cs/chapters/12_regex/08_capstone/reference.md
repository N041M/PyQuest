Závěrečná úloha skládá kapitolu: jediný vzor s **více zachytávacími skupinami**,
předaný **`re.findall`**, extrahuje strukturované záznamy v jednom kroku.

- S více než jednou skupinou vrátí `re.findall` seznam **n-tic** — jednu na shodu,
  držící text každé skupiny: `re.findall(r"(\w+)=(\w+)", s)` dá
  `[(klíč, hodnota), ...]`.
- Seznam dvojic `(klíč, hodnota)` je přesně to, co **`dict(...)`** konzumuje, takže
  `dict(re.findall(...))` je úplný mini-parser.
- `\w+` odpovídá úseku znaků slova (písmena, číslice, podtržítko); `=` mezi skupinami
  se shoduje **doslovně**. Žádná shoda dá `[]`, takže prázdný vstup čistě dá `{}`.

To je odměna regexu: popiš tvar jednoho záznamu a engine za tebe najde a rozebere
každý výskyt.

```python
import re

dict(re.findall(r"(\w+)=(\w+)", "host=local port=8080"))
# {'host': 'local', 'port': '8080'}
```
