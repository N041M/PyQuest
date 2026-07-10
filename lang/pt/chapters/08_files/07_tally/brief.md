# 8.7 -- Um relatório de frequências

## Conceito

Esta puzzle junta o capítulo com a contagem por dicionário de 5.9: lê um
ficheiro, **conta** algo ao longo dele, e escreve o resultado noutro
ficheiro.

Lê as palavras, depois conta-as com um dicionário (o padrão `dict.get`):

```python
with open("words.txt") as f:
    words = f.read().split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
```

`f.read().split()` lê o ficheiro inteiro e divide-o em qualquer espaço em
branco, dando-te assim uma lista simples de palavras, fosse qual fosse o seu
espaçamento.

Depois escreve o relatório, **ordenado por contagem, do maior para o menor**,
com empates desfeitos alfabeticamente. `sorted` com uma `key` (5.4) faz as
duas coisas de uma vez:

```python
for w in sorted(counts, key=lambda w: (-counts[w], w)):
    f.write(f"{w}: {counts[w]}\n")
```

A chave `(-counts[w], w)` ordena por contagem decrescente (negando-a) e depois
pela própria palavra em caso de empate.

## Exemplo

Um `words.txt` de `fig fig pear fig pear` torna-se num `report.txt` de:

```
fig: 3
pear: 2
```

## A tua tarefa

Conta quantas vezes cada palavra aparece em `words.txt`, e escreve
`report.txt` com uma linha `word: count` por palavra distinta -- ordenada por
contagem (a mais alta primeiro), com empates por ordem alfabética.

## Está feito quando

- Cada palavra distinta aparece uma vez, como `word: count`.
- As linhas estão ordenadas por contagem decrescente, alfabética dentro de um
  empate.
- Usaste `with`, um dicionário para contar, e leste as palavras do ficheiro.
