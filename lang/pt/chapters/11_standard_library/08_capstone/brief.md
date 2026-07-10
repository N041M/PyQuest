# 11.8 -- Capstone: um resumo estatístico a partir de JSON

## Conceito

A verdadeira lição deste capítulo é que o trabalho do dia a dia é
**compor ferramentas de biblioteca**: deixa um módulo ler os dados, outro
processá-los, e devolve o resultado. Aqui combinas dois dos módulos que
acabaste de conhecer.

A entrada é uma **string JSON** que contém uma lista de números, por
exemplo `"[4, 8, 15, 16]"`. Vais:

1. interpretá-la com **`json.loads`** para uma lista Python,
2. resumi-la com **`statistics`** e os nativos `max` / `min`,
3. devolver um dict simples com os resultados.

```python
import json
import statistics

data = json.loads("[4, 8, 15, 16]")     # [4, 8, 15, 16]
statistics.mean(data)                    # 10.75
```

## A tua tarefa

Define `summary(numbers_json)` que recebe uma string JSON de uma lista de
números e devolve um dict com estas chaves:

- `"count"` -- quantos números (`len`),
- `"mean"` -- a sua média (`statistics.mean`),
- `"max"` -- o maior (`max`),
- `"min"` -- o menor (`min`).

Interpreta a entrada com `json.loads`. Assume pelo menos um número.

## Está feito quando

- `summary("[2, 4, 6]")` é igual a
  `{"count": 3, "mean": 4, "max": 6, "min": 2}`.
- `summary("[5]")` é igual a `{"count": 1, "mean": 5, "max": 5, "min": 5}`.
- A entrada é interpretada com `json.loads`, não à mão.
