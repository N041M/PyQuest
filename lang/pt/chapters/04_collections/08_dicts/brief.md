# 4.8 -- Dicionários

## Conceito

Um **dicionário** (`dict`) associa **chaves** a **valores** -- uma tabela de
consulta. Escreve-se um com chavetas e pares `chave: valor`:

```python
ages = {"sam": 20, "ada": 36}
print(ages["sam"])     # 20      look up by key
ages["lee"] = 41       # add a new key
ages["sam"] = 21       # update an existing key
```

Procuram-se coisas pela **chave** (não pela posição), o que torna os dicionários
rápidos e úteis para "dado X, qual é o seu Y?". Começa vazio com `{}` e preenche-o:

```python
d = {}
d["x"] = 1
```

## Exemplo

```python
prices = {}
prices["apple"] = 3
print(prices["apple"])   # 3
```

## A tua tarefa

Lê uma contagem `n`, depois `n` pares de uma **palavra** e um **número** (palavra
numa linha, número na seguinte) para um dicionário (a palavra é a chave, o número o
valor). Depois lê mais uma **palavra de consulta** e imprime o número guardado
para ela.

Para a entrada `2`, `apple`, `3`, `banana`, `5`, seguida da consulta `banana`:

```
5
```

## Está feito quando

- Construir `{apple: 3, banana: 5}` e consultar `banana` imprime `5`.
- Um par posterior com a mesma chave atualiza-a (o teste depende do último valor
  para qualquer chave repetida).
