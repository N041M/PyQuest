Uma passagem de **filtragem** lê um ficheiro, mantém apenas as linhas que um
`if` aceita, e escreve-as noutro — a versão em ficheiros do padrão
compreensão-com-`if`.

- Abre a origem para leitura e o destino para escrita, percorre a origem, e só
  faz `f_out.write(line)` quando a linha passa no teu teste.
- As linhas da entrada mantêm a sua quebra de linha, por isso escrevê-las de
  volta reproduz as quebras de linha sem acrescentar nenhuma.
- Ler e escrever o **mesmo** caminho ao mesmo tempo não é seguro; escreve para
  um ficheiro novo (ou reúne os resultados e só depois escreve).

```python
with open("all.txt") as src, open("kept.txt", "w") as out:
    for line in src:
        if "ERROR" in line:
            out.write(line)       # keep only matching lines
```
