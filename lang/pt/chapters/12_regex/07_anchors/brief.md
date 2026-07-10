# 12.7 -- Âncoras: corresponder à cadeia de caracteres inteira

## Conceito

`re.search` fica satisfeito se o padrão aparecer **em qualquer lugar**. Para
**validar um formato**, precisas que a *cadeia de caracteres inteira*
corresponda -- sem caracteres sobrantes.

Duas formas de exigir isso:

- **Âncoras** no padrão: `^` prende-se ao **início**, `$` ao **fim**, por isso
  `r"^[A-Z]{2}\d{4}$"` tem de abranger a cadeia de caracteres inteira.
- **`re.fullmatch`**, que exige que o padrão cubra a cadeia de caracteres
  inteira por ti -- sem precisares de âncoras.

```python
import re

re.fullmatch(r"[A-Z]{2}\d{4}", "AB1234")     # matches
re.fullmatch(r"[A-Z]{2}\d{4}", "AB1234x")    # None -- trailing junk
re.search(r"[A-Z]{2}\d{4}", "AB1234x")       # matches -- search ignores the x
```

Aqui, um código de produto é duas letras maiúsculas seguidas de quatro
dígitos: `AB1234`.

## Exemplo

```python
import re

def is_word(text):
    return re.fullmatch(r"[a-z]+", text) is not None
```

## A tua tarefa

Usando **`re.fullmatch`** (ou `^...$`), define `is_valid_code(text)` que devolve
`True` apenas quando `text` é exatamente **duas letras maiúsculas seguidas de
quatro dígitos** (por exemplo, `"AB1234"`), `False` caso contrário.

## Está feito quando

- `is_valid_code("AB1234")` é `True`.
- `is_valid_code("ab1234")`, `is_valid_code("AB123")`, `is_valid_code("AB1234x")`
  são todos `False`.
- A cadeia de caracteres inteira é correspondida (fullmatch ou âncoras), não
  uma verificação de comprimento escrita à mão.
