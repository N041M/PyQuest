Um objeto de ficheiro é **iterável**: percorrê-lo num ciclo produz o ficheiro
**uma linha de cada vez**, sem carregar tudo para a memória. É a forma padrão
de processar um ficheiro linha a linha.

- `for line in f:` associa `line` a cada linha **incluindo a sua quebra de
  linha final** `"\n"`; chama `line.strip()` (ou `.rstrip("\n")`) para a
  remover.
- Lê de forma preguiçosa (*lazy*), por isso lida bem com ficheiros grandes.
- `f.readlines()`, em vez disso, devolve uma **lista** com todas as linhas de
  uma vez -- bom para ficheiros pequenos, dispendioso para os grandes.

```python
with open("log.txt") as f:
    for line in f:
        print(line.strip())   # one line per pass, newline removed
```
