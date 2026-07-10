# 8.8 -- Capítulo final: um relatório de classificação

## Conceito

Este capítulo final é um pequeno programa a sério: lê um ficheiro de
registos, classifica-os, e escreve um relatório formatado -- usando split
(4.4), desempacotamento (4.7), `int()` (1.11), `sorted` com uma key (5.4),
f-strings (2.10), e ficheiros (este capítulo), tudo junto.

`scores.txt` tem um registo por linha, um nome e uma pontuação separados por
um espaço:

```
alice 40
bob 25
cara 40
```

Cada linha divide-se nos seus dois campos:

```python
name, score = line.split()
score = int(score)
```

Queres que `ranking.txt` liste os jogadores da pontuação mais alta para a
mais baixa (empates por ordem alfabética), seguido de uma linha final de
total:

```
alice - 40
cara - 40
bob - 25
Total: 105
```

Repara no formato exato: `name - score` por jogador (espaços à volta do
travessão), e uma linha final de fecho `Total: <sum>`.

## A tua tarefa

Lê `scores.txt`, e escreve `ranking.txt` com uma linha `name - score` por
jogador ordenada por pontuação (a mais alta primeiro, empates por ordem
alfabética), seguida de uma linha final `Total: <soma de todas as
pontuações>`.

## Está feito quando

- Os jogadores estão listados como `name - score`, a pontuação mais alta
  primeiro, empates por ordem alfabética.
- A última linha é `Total: ` seguido da soma de todas as pontuações.
- Um ficheiro com um só jogador funciona, e usaste `with` para ambos os
  ficheiros.
