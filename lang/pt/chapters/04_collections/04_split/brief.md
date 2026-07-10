# 4.4 -- split: de texto para lista

## Conceito

`s.split()` divide uma cadeia de caracteres em **uma lista de partes**. Sem
argumentos, divide pelos espaços em branco, transformando assim uma frase nas suas
palavras:

```python
"the quick brown fox".split()    # ['the', 'quick', 'brown', 'fox']
```

O resultado é uma lista verdadeira, por isso tudo o que já sabes sobre listas se
aplica -- `len`, indexação, ciclos:

```python
words = "a b c".split()
print(len(words))    # 3
print(words[0])      # a
```

Também podes dividir por um separador específico passando-o como argumento:
`"a,b,c".split(",")` dá `['a', 'b', 'c']`.

## Exemplo

```python
parts = "one two three".split()
print(len(parts))    # 3
```

## A tua tarefa

Lê uma linha de palavras separadas por espaços, e imprime **quantas palavras** ela
contém.

Para a entrada `the quick brown fox`:

```
4
```

## Está feito quando

- `the quick brown fox` imprime `4`; uma única palavra imprime `1`.
- Uma linha vazia imprime `0`.
