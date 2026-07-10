# 12.1 -- re.search: o padrão está lá?

## Conceito

Uma **expressão regular** ("regex") é uma pequena linguagem para descrever padrões
em texto. O módulo **`re`** faz a correspondência com eles. A pergunta mais básica
é "este padrão aparece nalgum lugar?" -- **`re.search`**:

```python
import re

re.search(r"\d", "abc4")     # a match object (truthy)
re.search(r"\d", "abc")      # None
```

- O padrão é escrito como uma **cadeia de caracteres em bruto** `r"..."` para que
  as barras invertidas signifiquem o que o regex espera (`r"\d"`, não `"\d"`).
- `\d` corresponde a qualquer **dígito** único. Outros atalhos: `\w` um caractere
  de palavra, `\s` espaço em branco, `.` qualquer caractere.
- `re.search` devolve um **objeto de correspondência** se o padrão for encontrado
  nalgum lugar, ou **`None`** se não -- por isso `re.search(...) is not None` é
  um sim/não limpo.

## Exemplo

```python
import re

def has_letter(text):
    return re.search(r"[a-z]", text) is not None
```

## A tua tarefa

Usando **`re.search`**, define `has_digit(text)` que devolve `True` se `text`
contiver pelo menos um dígito, `False` caso contrário.

## Está feito quando

- `has_digit("abc4")` é `True`, `has_digit("abc")` é `False`.
- `has_digit("")` é `False`.
- O teste usa `re.search` com `\d`, não uma verificação de dígitos escrita à mão.
