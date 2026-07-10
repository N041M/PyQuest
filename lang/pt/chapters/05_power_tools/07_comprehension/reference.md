Uma **compreensão de lista** constrói uma nova lista numa só expressão: para cada `x` em
`items`, avalia `expr` e reúne os resultados, por ordem. É o
padrão construir-por-ciclo-e-append comprimido numa linha.

- `[expr for x in items]` equivale a começar com `result = []` e
  `result.append(expr)` num ciclo — o mesmo resultado, mais direto.
- `expr` pode ser qualquer expressão em `x`: `[n * n for n in nums]`,
  `[w.upper() for w in words]`.
- As compreensões também constroem conjuntos (`{...}`) e dicionários (`{k: v for ...}`).

```python
[n * n for n in range(5)]       # [0, 1, 4, 9, 16]
[w.upper() for w in ["a", "b"]] # ['A', 'B']
```
