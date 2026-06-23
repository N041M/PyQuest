**Regulární výraz** je vzor popisující množinu řetězců; modul **`re`** je hledá v
textu. **`re.search(pattern, text)`** prohledá celý řetězec a najde **první** místo,
kde vzor sedí, a vrátí **objekt shody** (který je pravdivý) nebo **`None`**.

- Vzory piš jako **surové řetězce** — `r"\d"` — aby zpětná lomítka dosáhla regexového
  enginu, místo aby je nejprve interpretoval Python.
- Zkratkové třídy: `\d` číslice, `\w` znak slova `[A-Za-z0-9_]`, `\s` bílý znak a `.`
  libovolný znak kromě nového řádku.
- `re.search` hledá **kdekoli** v řetězci; `re.match` kontroluje jen začátek.
  Protože výsledek je objekt shody nebo `None`, `re.search(...) is not None` je
  čistý test přítomnosti.

```python
import re

re.search(r"\d", "abc4")     # <re.Match object; match='4'>
re.search(r"\d", "abc")      # None
bool(re.search(r"\s", "a b"))  # True -- contains whitespace
```
