# 12.4 -- Quantificadores: + significa um ou mais

## Conceito

Um **quantificador** diz quantas vezes o padrão anterior pode repetir-se:

- **`+`** -- um ou mais (`[a-z]+` é uma sequência de uma ou mais letras
  minúsculas)
- **`*`** -- zero ou mais
- **`?`** -- opcional (zero ou um)
- **`{n}`** -- exatamente `n`; **`{n,m}`** -- entre `n` e `m`

```python
import re

re.findall(r"[A-Za-z]+", "Hello, world!")     # ['Hello', 'world']
```

Sem o `+`, `[A-Za-z]` corresponderia a letras únicas, uma de cada vez. O `+`
faz com que capture a **palavra inteira**, parando no primeiro caractere que
não se encaixe (um espaço, vírgula, dígito). É assim que se divide texto em
palavras ignorando a pontuação.

## Exemplo

```python
import re

def integers(text):
    return re.findall(r"\d+", text)
```

## A tua tarefa

Usando **`re.findall`** com um quantificador, define `find_words(text)` que
devolve uma lista das palavras em `text` -- cada uma uma sequência de uma ou
mais letras (`[A-Za-z]+`), ignorando pontuação e espaços.

## Está feito quando

- `find_words("Hello, world!")` devolve `["Hello", "world"]`.
- `find_words("one-two three")` devolve `["one", "two", "three"]`.
- `find_words("")` devolve `[]`.
- As palavras são correspondidas com `[A-Za-z]+`, não divididas à mão.
