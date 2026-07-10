Parênteses **`(...)`** num padrão criam um **grupo de captura** — uma
subparte da correspondência que o motor memoriza para que a possas ler depois.
O objeto de correspondência expõe-os:

- **`m.group(n)`** devolve o texto que o *n*-ésimo grupo capturou, numerado da
  esquerda para a direita a partir de 1; **`m.group(0)`** (ou `m.group()`) é a
  correspondência inteira.
- **`m.groups()`** devolve o texto de todos os grupos como um tuplo — ideal
  para desempacotar.
- O texto capturado é uma **cadeia de caracteres**; converte com `int(...)`
  conforme necessário. Um grupo que não participou é `None`.

Assim, um único padrão **valida** o formato e **extrai** os campos. `re.match`
ancora-se no início e devolve o objeto de correspondência ou `None`; protege-te
contra `None` antes de ler os grupos quando a entrada pode não corresponder.
Dá nomes aos grupos com `(?P<name>...)` e lê-os através de `m.group("name")`
para maior clareza.

```python
import re

m = re.match(r"(\d+)-(\d+)-(\d+)", "2026-06-20")
m.groups()                # ('2026', '06', '20')
tuple(int(p) for p in m.groups())   # (2026, 6, 20)
```
