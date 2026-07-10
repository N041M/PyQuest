# 1.2 -- Imprimir mais

## Conceito

Duas ideias novas, ambas sobre `print`.

**1. Vários prints correm por ordem.** Cada `print(...)` coloca o seu texto na sua própria linha,
e o Python corre-os de cima para baixo. Três linhas `print` produzem três linhas de saída.

**2. Um print pode mostrar vários valores.** Coloca várias coisas dentro dos
parênteses separadas por **vírgulas**, e o `print` mostra-as numa linha com um
único espaço entre cada uma:

```python
print("a", "b", "c")
```

mostra:

```
a b c
```

Podes misturar texto e números desta forma. Os números **não** precisam de aspas; o texto precisa.

## Exemplo

```python
print("Scores:")
print(10, 20, 30)
```

mostra:

```
Scores:
10 20 30
```

A primeira linha é um print; o segundo print tem três valores separados por
vírgulas, por isso partilham uma linha com espaços entre eles.

## A tua tarefa

Produz exatamente estas duas linhas:

```
Counting:
1 2 3
```

Usa duas instruções `print`: a primeira imprime a palavra, a segunda imprime os
três números `1`, `2`, `3` como valores separados (deixa o `print` acrescentar os espaços).

## Está feito quando

- O resultado é exatamente duas linhas: `Counting:` depois `1 2 3`.
- A segunda linha vem de números separados por vírgulas, não de escreveres tu mesmo
  o texto `"1 2 3"`.
