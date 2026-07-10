Um **quantificador** controla quantas vezes o padrão imediatamente anterior se
repete:

- **`+`** um ou mais, **`*`** zero ou mais, **`?`** zero ou um (opcional),
- **`{n}`** exatamente *n*, **`{n,m}`** entre *n* e *m*, **`{n,}`** pelo menos
  *n*.

`[A-Za-z]+` corresponde assim a uma **palavra** inteira — uma sequência de uma
ou mais letras — parando no primeiro caractere que não se encaixe, que é como
se tokeniza texto ignorando espaços e pontuação.

- Os quantificadores são **gulosos** por defeito: correspondem ao máximo
  possível. Um `?` final torna um deles **preguiçoso** (`\d+?` corresponde ao
  menor número de dígitos possível).
- O quantificador aplica-se ao único elemento anterior — um caractere, uma
  classe, ou um grupo entre parênteses: `(ab)+` corresponde a `ababab`.

```python
import re

re.findall(r"[A-Za-z]+", "Hello, world!")   # ['Hello', 'world']
re.findall(r"\d{4}", "y2024 y2025")          # ['2024', '2025']
re.search(r"colou?r", "color")               # matches (the u is optional)
```
