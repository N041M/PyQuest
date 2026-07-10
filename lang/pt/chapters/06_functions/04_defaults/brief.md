# 6.4 -- Valores por omissão

## Conceito

Um parâmetro pode ter um valor **por omissão**: o valor usado quando quem chama o
deixa de fora. Escreve-o com `=` na linha do `def`:

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Ada")              # "Hello, Ada!"   -- default used
greet("Ada", "Hi")        # "Hi, Ada!"      -- default overridden
```

Já *usaste* isto: `print(..., sep=" ")` de 1.3 -- `sep` tem um valor
por omissão de um espaço, que substituíste com `sep=", "`. Agora podes construir
a mesma flexibilidade nas tuas próprias funções.

Regras: os parâmetros com valores por omissão vêm **depois** dos que não têm, e o
valor por omissão só é usado quando quem chama omite esse argumento.

## Exemplo

```python
def repeat(word, times=2):
    return word * times

repeat("ha")        # "haha"
repeat("ha", 3)     # "hahaha"
```

## A tua tarefa

Define `greet(name, greeting="Hello")` que devolva `"<greeting>, <name>!"` --
exatamente: o cumprimento, uma vírgula e um espaço, o nome, um ponto de exclamação.

## Está feito quando

- `greet("Ada")` devolve `"Hello, Ada!"` (o valor por omissão em ação).
- `greet("Ada", "Hi")` devolve `"Hi, Ada!"`.
- Sem o valor por omissão, a chamada com um só argumento rebentaria -- o verificador faz
  os dois tipos de chamada.
