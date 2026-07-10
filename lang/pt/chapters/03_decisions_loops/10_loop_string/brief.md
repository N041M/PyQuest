# 3.10 -- Percorrer uma string

## Conceito

Um ciclo `for` funciona com mais do que intervalos. Uma **string é uma sequência de
caracteres**, por isso podes percorrê-la diretamente -- um carácter por passagem:

```python
for ch in "cat":
    print(ch)
# prints:
# c
# a
# t
```

Não é preciso indexar: `ch` é, sucessivamente, cada carácter. (Podes percorrer
muitos tipos de sequências desta forma; as strings são o primeiro exemplo.)

## Exemplo

```python
word = "hi"
for ch in word:
    print(ch)
# prints h then i
```

## A tua tarefa

Lê uma palavra e imprime cada um dos seus caracteres na sua própria linha, usando
um ciclo `for` sobre a string.

Para a entrada `cat` a saída é:

```
c
a
t
```

## Está feito quando

- `cat` imprime `c`, `a`, `t` em linhas separadas.
- Uma única letra imprime essa letra; uma entrada vazia não imprime nada.
