O capítulo final lê **registos**, interpreta cada um em campos utilizáveis,
classifica-os, e escreve um **relatório formatado** — a forma do trabalho real
com dados.

- **Interpretar**: divide cada linha em campos e converte os tipos (por
  exemplo `name, score = line.split(","); score = int(score)`), reunindo os
  registos numa lista.
- **Classificar**: `sorted(records, key=..., reverse=True)` ordena pelo campo
  que importa.
- **Formatar**: escreve linhas alinhadas e legíveis por humanos, usando
  larguras de campo em f-strings (`f"{name:<12}{score:>5}"`) para que as
  colunas fiquem alinhadas.

```python
records = []
with open("scores.csv") as f:
    for line in f:
        name, score = line.strip().split(",")
        records.append((name, int(score)))
with open("ranked.txt", "w") as out:
    for name, score in sorted(records, key=lambda r: r[1], reverse=True):
        out.write(f"{name:<12}{score:>5}\n")
```
