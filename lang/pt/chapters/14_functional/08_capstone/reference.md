O capstone encadeia as funções de ordem superior do capítulo num **pipeline
de dados** — a forma de muito processamento real:

1. **`filter(lambda r: r[1] >= threshold, records)`** restringe aos registos
   que se qualificam;
2. **`sorted(..., key=lambda r: r[1], reverse=True)`** classifica-os por
   pontuação, do mais alto para o mais baixo (estável, por isso pontuações
   iguais mantêm a sua ordem);
3. **`map(lambda r: r[0], ...)`** projeta apenas o campo que queres — o nome.

Cada etapa recebe uma função e um iterável e produz outro iterável, por isso
compõem-se diretamente: o filter alimenta o sort, o sort alimenta o map. O
mesmo pipeline podia ser escrito com compreensões; expressá-lo como
`filter`/`sorted`/`map` é o estilo funcional, e ver uma tarefa *como* um
pipeline de transformações é a competência para a qual o capítulo conduz.

```python
def passing(records, threshold):
    qualified = filter(lambda r: r[1] >= threshold, records)
    ranked = sorted(qualified, key=lambda r: r[1], reverse=True)
    return list(map(lambda r: r[0], ranked))
```
