Por defeito, um padrão pode corresponder **em qualquer lugar** da cadeia de
caracteres. Validar um *formato* significa que a cadeia de caracteres
**inteira** tem de estar conforme — sem caracteres sobrantes. Duas formas de
exigir isso:

- **Âncoras** no padrão: **`^`** corresponde ao início da cadeia de
  caracteres, **`$`** ao fim. `r"^[A-Z]{2}\d{4}$"` tem de abranger toda a
  entrada.
- **`re.fullmatch(pattern, text)`** exige que o padrão cubra a cadeia de
  caracteres inteira por ti — sem precisares de âncoras. Devolve um objeto de
  correspondência ou `None`.

O contraste: `re.search(r"[A-Z]{2}\d{4}", "AB1234x")` **corresponde** (o
padrão ocorre), mas `re.fullmatch(r"[A-Z]{2}\d{4}", "AB1234x")` é **`None`**
(o `x` sobra). Usa `search`/`findall` para *encontrar* subcadeias,
`fullmatch`/âncoras para *validar* um valor inteiro.

```python
import re

bool(re.fullmatch(r"[A-Z]{2}\d{4}", "AB1234"))    # True
bool(re.fullmatch(r"[A-Z]{2}\d{4}", "AB1234x"))   # False
bool(re.match(r"^\d{5}$", "12345"))               # True -- anchored form
```
