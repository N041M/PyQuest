# 12.2 -- re.findall: todas as correspondências

## Conceito

`re.search` encontra a *primeira* correspondência. **`re.findall`** devolve
**todas** elas, como uma lista de cadeias de caracteres:

```python
import re

re.findall(r"\d+", "a12b3c456")     # ['12', '3', '456']
```

- `\d+` significa "um ou mais dígitos" -- o `+` faz o padrão capturar uma
  sequência inteira de dígitos, não apenas um. Assim, cada correspondência é um
  número completo.
- `re.findall` devolve uma **lista de cadeias de caracteres** (o texto
  correspondido), da esquerda para a direita, sem sobreposição. Nenhuma
  correspondência dá a lista vazia `[]`.
- As correspondências continuam a ser texto; converte com `int(...)` se
  quiseres números.

## Exemplo

```python
import re

def words(text):
    return re.findall(r"[a-z]+", text)
```

## A tua tarefa

Usando **`re.findall`**, define `all_numbers(text)` que devolve uma lista de
cada sequência de dígitos em `text`, como cadeias de caracteres.

## Está feito quando

- `all_numbers("a12b3c456")` devolve `["12", "3", "456"]`.
- `all_numbers("nothing")` devolve `[]`.
- A extração usa `re.findall` com `\d+`, não uma verificação escrita à mão.
