# 5.10 -- Capítulo final: relatório de palavras

## Conceito

Nada de novo desta vez -- este puzzle combina o capítulo (e o capítulo 4) num
único programa pequeno e real: um **relatório de frequência de palavras**, o coração de
todas as funcionalidades de "palavras mais comuns" que já viste.

As peças, todas as quais já tens:

- `.split()` -- a linha em palavras (4.4)
- o padrão de contagem -- contar cada palavra (5.9)
- `sorted()` -- ordenar o relatório (5.4). Uma nova conveniência: percorrer um
  dicionário visita as suas **chaves**, por isso `sorted(counts)` são simplesmente as chaves em
  ordem alfabética.
- imprimir uma palavra e a sua contagem numa linha (1.2)

## Exemplo

Para a linha `b a b`:

```python
counts = {"b": 2, "a": 1}
for w in sorted(counts):
    print(w, counts[w])
# a 1
# b 2
```

## A tua tarefa

Lê uma linha de palavras. Imprime uma linha por palavra **distinta** -- a palavra, um
espaço, e quantas vezes apareceu -- em ordem **alfabética**.

Para a entrada `tea milk tea`:

```
milk 1
tea 2
```

## Está feito quando

- `tea milk tea` imprime `milk 1` depois `tea 2` -- palavras distintas, ordem alfabética.
- Uma única palavra repetida imprime uma linha com a sua contagem total.
- Uma linha vazia não imprime nada.
- Usaste uma contagem com dicionário e `sorted()`.
