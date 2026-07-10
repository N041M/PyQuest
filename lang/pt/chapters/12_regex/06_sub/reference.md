**`re.sub(pattern, repl, text)`** é uma pesquisa-e-substituição orientada por
padrão: devolve uma **nova** cadeia de caracteres com **todas** as
correspondências sem sobreposição de `pattern` substituídas por `repl`. Onde
`str.replace` troca uma subcadeia fixa, `re.sub` troca tudo o que o padrão
descreve.

- Como um padrão quantificado corresponde a uma **sequência**, cada sequência
  reduz-se a uma substituição: `re.sub(r"\d+", "#", "a12b3")` é `"a#b#"`, não
  `"a##b#"`.
- Sem correspondência, o texto fica inalterado. Um `count=` opcional limita
  quantas substituições são feitas.
- `repl` pode referenciar grupos capturados com `\1`, `\2`, … (por exemplo,
  `re.sub(r"(\w+)@(\w+)", r"\2.\1", s)`), ou ser uma **função** que recebe cada
  correspondência e devolve a sua substituição, para lógica demasiado
  complexa para um modelo.

```python
import re

re.sub(r"\s+", " ", "too   many    spaces")   # 'too many spaces'
re.sub(r"\d+", "#", "call 555-1234")           # 'call #-#'
re.sub(r"(\d+)", r"[\1]", "x12")               # 'x[12]'
```
