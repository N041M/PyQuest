# 14.8 -- Capstone: uma lista restrita classificada

## Conceito

As ferramentas do capítulo encadeiam-se num **pipeline**. Dada uma lista de
registos `(name, score)`, constrói uma lista restrita:

1. **`filter`** para os registos que atingem um limiar,
2. **`sorted`** com um `key=lambda` (e `reverse=True`) para os classificar do
mais alto para o mais baixo,
3. **`map`** para extrair apenas os nomes.

```python
records = [("Ada", 90), ("Linus", 70), ("Grace", 95)]
qualified = filter(lambda r: r[1] >= 80, records)
ranked = sorted(qualified, key=lambda r: r[1], reverse=True)
list(map(lambda r: r[0], ranked))     # ['Grace', 'Ada']
```

Cada registo é um tuplo, por isso `r[0]` é o nome e `r[1]` a pontuação.

## A tua tarefa

Define `passing(records, threshold)` que recebe uma lista de tuplos `(name,
score)` e devolve os **nomes** daqueles com `score >= threshold`, ordenados
pela pontuação **da mais alta para a mais baixa**, construído com `filter`,
`sorted(key=lambda ...)`, e `map`.

## Está feito quando

- `passing([("Ada", 90), ("Linus", 70), ("Grace", 95)], 80)` devolve
  `["Grace", "Ada"]`.
- `passing([], 50)` devolve `[]`; um limiar acima de todas as pontuações
  devolve `[]`.
- O resultado é construído filtrando, ordenando por uma chave lambda, e
  mapeando -- um pipeline das ferramentas do capítulo.
