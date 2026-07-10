# 12.6 -- re.sub: encontrar e substituir por padrão

## Conceito

`str.replace` troca uma subcadeia fixa. **`re.sub`** troca tudo o que
corresponda a um **padrão**:

```python
import re

re.sub(r"\d+", "#", "call 555-1234 now")     # 'call #-# now'
```

- `re.sub(pattern, replacement, text)` devolve uma **nova** cadeia de
  caracteres com **todas** as correspondências de `pattern` substituídas por
  `replacement`.
- Como `\d+` corresponde a uma sequência inteira de dígitos, cada sequência
  reduz-se a um único `#` -- uma substituição por correspondência, não por
  caractere.
- Sem correspondência, o texto fica inalterado. A substituição também pode
  referenciar grupos capturados (`\1`), mas uma cadeia de caracteres simples é
  o caso mais comum.

## Exemplo

```python
import re

def squash_spaces(text):
    return re.sub(r"\s+", " ", text)
```

## A tua tarefa

Usando **`re.sub`**, define `redact(text)` que substitui cada sequência de
dígitos em `text` por um único `"#"`.

## Está feito quando

- `redact("call 555-1234")` devolve `"call #-#"`.
- `redact("no digits")` devolve `"no digits"`.
- Cada *sequência* de dígitos torna-se um `#` (usa `\d+`), através de `re.sub`
  -- não um ciclo de caracteres.
