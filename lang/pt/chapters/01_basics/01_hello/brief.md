# 1.1 -- Hello, output

## Conceito

Um **programa** é uma lista de instruções que o computador executa de cima para baixo.
A instrução mais básica é **imprimir** -- colocar uma linha de texto no
ecrã. Em Python fazes isso com `print(...)`. Tudo o que colocares dentro dos
parênteses, entre aspas, é mostrado.

`print` é uma **função**: uma ação nativa que ativas escrevendo o seu nome
seguido de parênteses. O que está entre aspas é **texto** (o Python chama texto de
*cadeia de caracteres* -- uma sequência de caracteres).

## Exemplo

```python
print("Good morning")
```

Quando isto corre, o ecrã mostra:

```
Good morning
```

As aspas marcam onde o texto começa e acaba; elas próprias não são impressas. O Python
também acrescenta automaticamente uma quebra de linha no final, por isso o próximo print
começa numa linha nova.

## A tua tarefa

Faz o programa imprimir exatamente esta linha:

```
Hello, output
```

Abre o ficheiro de trabalho do capítulo `work.py`, escreve um `print(...)` que produza essa
linha, **guarda o ficheiro**, e depois corre `check`.

## Está feito quando

- Correr `check` mostra CHECK PASSED.
- O resultado é `Hello, output` -- as mesmas palavras, a mesma vírgula. (A verificação
  ignora maiúsculas/minúsculas, mas seguir o enunciado à risca é um bom hábito.)
