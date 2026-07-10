# 5.6 -- zip(): emparelhar listas

## Conceito

Duas listas muitas vezes andam juntas item a item: nomes e pontuações, perguntas e
respostas. `zip()` percorre-as **em sincronia**, entregando-te um par por passagem:

```python
names = ["amy", "ben"]
scores = [90, 85]
for name, score in zip(names, scores):
    print(name, score)
# amy 90
# ben 85
```

Como o `enumerate`, cada passagem dá um par que desempacotas em duas variáveis.
O nome vem da imagem de um fecho de correr: duas filas de dentes unidas uma a uma.

Se as listas tiverem comprimentos diferentes, o `zip` para na **mais curta** --
os itens extra na lista mais longa simplesmente nunca são visitados.

## Exemplo

```python
for a, b in zip("ab", [1, 2]):
    print(a, b)
# a 1
# b 2
```

## A tua tarefa

Lê uma contagem `n`, depois `n` nomes, depois `n` pontuações (números inteiros). Imprime uma
linha por par: o nome, um espaço, a pontuação.

Para a entrada `2`, depois `amy`, `ben`, depois `90`, `85`:

```
amy 90
ben 85
```

## Está feito quando

- Dois nomes e duas pontuações imprimem-se como duas linhas `nome pontuação`, por ordem.
- Uma contagem de `0` não imprime nada.
- Usaste `zip()` para emparelhar as duas listas.
