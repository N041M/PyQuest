Um **relatório de frequências** é um pipeline de ficheiros em três etapas:
**ler** o ficheiro, **contar** para um dicionário, e depois **escrever** um
resumo ordenado.

- Percorre as linhas (ou palavras), contando com
  `counts[k] = counts.get(k, 0) + 1`.
- Ordena o resultado com `sorted(counts.items(), ...)` — por chave, ou por
  contagem com `key=lambda kv: kv[1]` (acrescenta `reverse=True` para a mais
  frequente primeiro).
- Escreve cada par como uma linha formatada, por exemplo
  `out.write(f"{word}: {n}\n")`.

Compõe a E/S de ficheiros deste capítulo com as ferramentas de dicionário e
`sorted` de capítulos anteriores.

```python
counts = {}
with open("words.txt") as f:
    for line in f:
        w = line.strip()
        counts[w] = counts.get(w, 0) + 1
with open("report.txt", "w") as out:
    for w, n in sorted(counts.items()):
        out.write(f"{w}: {n}\n")
```
