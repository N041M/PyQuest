# 11.4 -- random: acaso reprodutível

## Conceito

O módulo **`random`** produz valores pseudoaleatórios: `random.randint(1, 6)`
lança um dado, `random.shuffle(lst)` reordena uma lista no próprio local. São *pseudo*-
aleatórios -- calculados a partir de um estado interno -- o que significa que os podes tornar
**repetíveis** fixando esse estado com uma **seed**:

```python
import random

random.seed(42)
random.shuffle(deck)     # always the same order for seed 42
```

- `random.seed(n)` define o ponto de partida. Com a mesma seed, as mesmas
  chamadas produzem os mesmos resultados, em toda a execução, em toda a
  máquina.
- `random.shuffle(lst)` baralha **no próprio local** (devolve `None`), por
  isso baralha uma cópia se precisares de manter o original.

Definir a seed é a forma como um jogo repete um nível, ou como um teste verifica
código "aleatório".

## Exemplo

```python
import random

def pick(options, seed):
    random.seed(seed)
    return random.choice(options)
```

## A tua tarefa

Define `shuffled(items, seed)` que devolve uma lista **nova** com os itens
de `items` baralhados, tornada repetível ao definir a seed com `seed`
**antes** de baralhar. Não alteres o `items` original.

## Está feito quando

- `shuffled(items, seed)` dá o mesmo resultado todas as vezes para os mesmos
  `items` e `seed`.
- A lista original passada fica inalterada (baralha uma cópia).
- `shuffled([], 1)` devolve `[]`.
