# 1.6 -- Reatribuir uma variável

## Conceito

Uma variável pode ser **alterada** depois de criada. Atribuir de novo ao mesmo nome
substitui o valor antigo por um novo. O nome refere-se sempre ao que
foi guardado **mais recentemente**.

```python
x = 10
print(x)   # 10
x = 20
print(x)   # 20
```

A ordem importa: o programa corre de cima para baixo, por isso o primeiro `print(x)` vê
`10`, e só depois da segunda atribuição é que `x` passa a `20`.

Um padrão comum e útil é atualizar uma variável usando o seu próprio valor atual:

```python
x = 10
x = x + 5   # take the current x (10), add 5, store 15 back in x
print(x)    # 15
```

O lado direito é calculado primeiro (`10 + 5`), e só depois o resultado é guardado de volta
em `x`.

## Erro comum

Reatribuir não cria uma segunda variável. Continua a haver apenas um `x`; o seu valor
guardado foi trocado. O valor antigo simplesmente desaparece.

## A tua tarefa

Cria uma variável com o valor `10` e imprime-a. Depois reatribui essa mesma variável para
`20` e imprime-a outra vez. O resultado tem de ser:

```
10
20
```

## Está feito quando

- O resultado é `10` depois `20` em duas linhas.
- Ambas as linhas imprimem a **mesma** variável, antes e depois de a alterares.
